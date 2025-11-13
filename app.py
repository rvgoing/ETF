from flask import Flask, render_template, request
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

def calculate_investment(total_monthly, years, r_2330, r_0050, r_00770, plot_height):
    """計算投資數據並生成圖表"""
    
    # 固定比例分配
    ratio_2330 = 0.50
    ratio_0050 = 0.30
    ratio_00770 = 0.20
    
    # 計算各標的金額
    p_2330 = int(total_monthly * ratio_2330)
    p_0050 = int(total_monthly * ratio_0050)
    p_00770 = int(total_monthly * ratio_00770)
    
    months = years * 12
    
    # 轉換年化報酬率
    P = np.array([p_2330, p_0050, p_00770])
    annual_rates = np.array([r_2330/100, r_0050/100, r_00770/100])
    monthly_rates = annual_rates / 12
    
    # 每月累積資產
    fv_2330 = np.zeros(months)
    fv_0050 = np.zeros(months)
    fv_00770 = np.zeros(months)
    
    for i in range(months):
        fv_2330[i] = P[0] * ((1 + monthly_rates[0])**(i+1) - 1) / monthly_rates[0] if monthly_rates[0] > 0 else P[0] * (i+1)
        fv_0050[i] = P[1] * ((1 + monthly_rates[1])**(i+1) - 1) / monthly_rates[1] if monthly_rates[1] > 0 else P[1] * (i+1)
        fv_00770[i] = P[2] * ((1 + monthly_rates[2])**(i+1) - 1) / monthly_rates[2] if monthly_rates[2] > 0 else P[2] * (i+1)
    
    fv_total = fv_2330 + fv_0050 + fv_00770
    
    # 計算指標
    total_invested = sum(P) * months
    total_asset = fv_total[-1]
    total_profit = total_asset - total_invested
    profit_rate = (total_profit / total_invested * 100) if total_invested > 0 else 0
    
    # 生成圖表
    fig, ax = plt.subplots(figsize=(12, plot_height))
    ax.plot(fv_2330, label='2330 - 台積電', linewidth=2.5)
    ax.plot(fv_0050, label='0050 - 元大台灣50 ETF', linewidth=2.5)
    ax.plot(fv_00770, label='00770 - 國泰北美科技 ETF', linewidth=2.5)
    ax.plot(fv_total, label='總資產', linestyle='--', color='black', linewidth=3)
    ax.set_title(f'{years} 年累積資產成長模擬', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('月數', fontsize=14)
    ax.set_ylabel('累積資產 (NTD)', fontsize=14)
    ax.legend(loc='upper left', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
    
    # 轉換圖表為 base64
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight', dpi=100)
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return {
        'p_2330': p_2330,
        'p_0050': p_0050,
        'p_00770': p_00770,
        'monthly_total': sum(P),
        'total_invested': total_invested,
        'total_asset': total_asset,
        'total_profit': total_profit,
        'profit_rate': profit_rate,
        'fv_2330_final': fv_2330[-1],
        'fv_0050_final': fv_0050[-1],
        'fv_00770_final': fv_00770[-1],
        'plot_url': plot_url
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    # 預設值
    default_values = {
        'total_monthly': 14500,
        'years': 10,
        'r_2330': 8.0,
        'r_0050': 6.0,
        'r_00770': 10.0,
        'plot_height': 8
    }
    
    if request.method == 'POST':
        # 取得表單數據
        total_monthly = int(request.form.get('total_monthly', default_values['total_monthly']))
        years = int(request.form.get('years', default_values['years']))
        r_2330 = float(request.form.get('r_2330', default_values['r_2330']))
        r_0050 = float(request.form.get('r_0050', default_values['r_0050']))
        r_00770 = float(request.form.get('r_00770', default_values['r_00770']))
        plot_height = int(request.form.get('plot_height', default_values['plot_height']))
        
        # 計算結果
        results = calculate_investment(total_monthly, years, r_2330, r_0050, r_00770, plot_height)
        
        return render_template('index.html', 
                             results=results,
                             values={
                                 'total_monthly': total_monthly,
                                 'years': years,
                                 'r_2330': r_2330,
                                 'r_0050': r_0050,
                                 'r_00770': r_00770,
                                 'plot_height': plot_height
                             })
    
    return render_template('index.html', values=default_values)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)