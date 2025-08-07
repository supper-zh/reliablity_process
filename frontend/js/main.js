// 制程可靠性数据分析系统前端逻辑

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // HCI&NBTI数据查询按钮事件
    document.getElementById('search-hci-nbti').addEventListener('click', function() {
        searchHciNbtiData();
    });
    
    // HCI&NBTI数据导出按钮事件
    document.getElementById('export-hci-nbti').addEventListener('click', function() {
        exportHciNbtiData();
    });
    
    // VRDB数据查询按钮事件
    document.getElementById('search-vrdb').addEventListener('click', function() {
        searchVrdbData();
    });
    
    // VRDB数据导出按钮事件
    document.getElementById('export-vrdb').addEventListener('click', function() {
        exportVrdbData();
    });
    
    // VRDB散点图显示按钮事件
    document.getElementById('show-scatter-plot').addEventListener('click', function() {
        showVrdbScatterPlot();
    });
    
    // TDDB数据查询按钮事件
    document.getElementById('search-tddb').addEventListener('click', function() {
        searchTddbData();
    });
    
    // TDDB数据导出按钮事件
    document.getElementById('export-tddb').addEventListener('click', function() {
        exportTddbData();
    });
    
    // TDDB散点图显示按钮事件
    document.getElementById('show-scatter-plot-tddb').addEventListener('click', function() {
        showTddbScatterPlot();
    });
    
    // Wafer热力图显示按钮事件
    document.getElementById('show-wafer-heatmap').addEventListener('click', function() {
        showWaferHeatmap();
    });
    
    // 报告生成按钮事件
    document.getElementById('generate-report').addEventListener('click', function() {
        generateReport();
    });
    
    // 报告下载按钮事件
    document.getElementById('download-report').addEventListener('click', function() {
        downloadReport();
    });
    
    // 为所有输入框添加回车键事件
    const inputs = document.querySelectorAll('input[type="text"], input[type="date"]');
    inputs.forEach(input => {
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                // 找到最近的查询按钮并点击
                const section = this.closest('section');
                const searchButton = section.querySelector('button[id^="search"]');
                if (searchButton) {
                    searchButton.click();
                }
            }
        });
    });
});

// 显示加载状态
function showLoading(elementId) {
    const element = document.getElementById(elementId);
    element.innerHTML = `
        <div style="text-align: center; padding: 2rem;">
            <div class="loading"></div>
            <p style="margin-top: 1rem; color: #666;">数据加载中...</p>
        </div>
    `;
}

// 显示错误信息
function showError(elementId, message) {
    const element = document.getElementById(elementId);
    element.innerHTML = `
        <div style="text-align: center; padding: 2rem; color: #e74c3c;">
            <i class="fas fa-exclamation-triangle fa-2x"></i>
            <p style="margin-top: 1rem;">${message}</p>
        </div>
    `;
}

// 查询HCI&NBTI数据
function searchHciNbtiData() {
    const lotId = document.getElementById('lot-id').value;
    const deviceName = document.getElementById('device-name').value;
    
    // 显示加载状态
    showLoading('hci-nbti-table');
    
    // 这里应该调用后端API获取数据
    console.log('查询HCI&NBTI数据:', { lotId, deviceName });
    
    // 模拟API调用延迟
    setTimeout(() => {
        // 模拟数据
        const mockData = [
            { id: 1, lot_id: 'LOT001', device_id: 'DEV001', device_name: 'Device A', std: 'STD001', vtd: 1.23 },
            { id: 2, lot_id: 'LOT002', device_id: 'DEV002', device_name: 'Device B', std: 'STD002', vtd: 2.34 },
            { id: 3, lot_id: 'LOT003', device_id: 'DEV003', device_name: 'Device C', std: 'STD003', vtd: 3.45 },
            { id: 4, lot_id: 'LOT004', device_id: 'DEV004', device_name: 'Device D', std: 'STD004', vtd: 4.56 }
        ];
        
        displayHciNbtiTable(mockData);
    }, 1000);
}

// 显示HCI&NBTI数据表格
function displayHciNbtiTable(data) {
    const tableContainer = document.getElementById('hci-nbti-table');
    
    if (data.length === 0) {
        tableContainer.innerHTML = `
            <div style="text-align: center; padding: 2rem; color: #7f8c8d;">
                <i class="fas fa-info-circle fa-2x"></i>
                <p style="margin-top: 1rem;">未找到相关数据</p>
            </div>
        `;
        return;
    }
    
    let tableHtml = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Lot ID</th>
                    <th>设备ID</th>
                    <th>设备名称</th>
                    <th>STD</th>
                    <th>VTD</th>
                    <th>操作</th>
                </tr>
            </thead>
            <tbody>
    `;
    
    data.forEach(item => {
        tableHtml += `
            <tr>
                <td>${item.id}</td>
                <td>${item.lot_id}</td>
                <td>${item.device_id}</td>
                <td>${item.device_name}</td>
                <td>${item.std}</td>
                <td>${item.vtd}</td>
                <td>
                    <button class="action-btn" onclick="viewDetails(${item.id})">
                        <i class="fas fa-eye"></i> 查看详情
                    </button>
                </td>
            </tr>
        `;
    });
    
    tableHtml += `
            </tbody>
        </table>
    `;
    
    tableContainer.innerHTML = tableHtml;
}

// 导出HCI&NBTI数据
function exportHciNbtiData() {
    // 获取查询条件
    const lotId = document.getElementById('lot-id').value;
    const deviceName = document.getElementById('device-name').value;
    
    // 显示加载状态
    const exportBtn = document.getElementById('export-hci-nbti');
    const originalText = exportBtn.innerHTML;
    exportBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> 导出中...';
    exportBtn.disabled = true;
    
    // 构造请求参数
    const params = new URLSearchParams();
    if (lotId) params.append('lot_id', lotId);
    if (deviceName) params.append('device_name', deviceName);
    
    // 模拟导出过程
    setTimeout(() => {
        // 恢复按钮状态
        exportBtn.innerHTML = originalText;
        exportBtn.disabled = false;
        
        // 显示成功消息
        alert('HCI&NBTI数据已成功导出!');
        
        // 这里应该实际调用后端导出接口
        // window.location.href = `/api/hci-nbti/export?${params.toString()}`;
    }, 1500);
}

// 查询VRDB数据
function searchVrdbData() {
    const deviceId = document.getElementById('vrdb-device-id').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    
    // 显示加载状态
    showLoading('vrdb-table');
    
    // 这里应该调用后端API获取数据
    console.log('查询VRDB数据:', { deviceId, startDate, endDate });
    
    // 模拟API调用延迟
    setTimeout(() => {
        // 模拟数据
        const mockData = [
            { id: 1, device_id: 'DEV001', voltage: 3.3, current: 0.5, resistance: 6.6 },
            { id: 2, device_id: 'DEV002', voltage: 5.0, current: 0.8, resistance: 6.25 },
            { id: 3, device_id: 'DEV003', voltage: 3.0, current: 0.6, resistance: 5.0 },
            { id: 4, device_id: 'DEV004', voltage: 4.5, current: 0.7, resistance: 6.4 }
        ];
        
        displayVrdbTable(mockData);
    }, 1000);
}

// 显示VRDB数据表格
function displayVrdbTable(data) {
    const tableContainer = document.getElementById('vrdb-table');
    
    if (data.length === 0) {
        tableContainer.innerHTML = `
            <div style="text-align: center; padding: 2rem; color: #7f8c8d;">
                <i class="fas fa-info-circle fa-2x"></i>
                <p style="margin-top: 1rem;">未找到相关数据</p>
            </div>
        `;
        return;
    }
    
    let tableHtml = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>设备ID</th>
                    <th>电压(V)</th>
                    <th>电流(A)</th>
                    <th>电阻(Ω)</th>
                    <th>操作</th>
                </tr>
            </thead>
            <tbody>
    `;
    
    data.forEach(item => {
        tableHtml += `
            <tr>
                <td>${item.id}</td>
                <td>${item.device_id}</td>
                <td>${item.voltage}</td>
                <td>${item.current}</td>
                <td>${item.resistance}</td>
                <td>
                    <button class="action-btn" onclick="viewVrdbDetails(${item.id})">
                        <i class="fas fa-eye"></i> 查看详情
                    </button>
                </td>
            </tr>
        `;
    });
    
    tableHtml += `
            </tbody>
        </table>
    `;
    
    tableContainer.innerHTML = tableHtml;
}

// 导出VRDB数据
function exportVrdbData() {
    // 获取查询条件
    const deviceId = document.getElementById('vrdb-device-id').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    
    // 显示加载状态
    const exportBtn = document.getElementById('export-vrdb');
    const originalText = exportBtn.innerHTML;
    exportBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> 导出中...';
    exportBtn.disabled = true;
    
    // 构造请求参数
    const params = new URLSearchParams();
    if (deviceId) params.append('device_id', deviceId);
    if (startDate) params.append('start_date', startDate);
    if (endDate) params.append('end_date', endDate);
    
    // 模拟导出过程
    setTimeout(() => {
        // 恢复按钮状态
        exportBtn.innerHTML = originalText;
        exportBtn.disabled = false;
        
        // 显示成功消息
        alert('VRDB数据已成功导出!');
        
        // 这里应该实际调用后端导出接口
        // window.location.href = `/api/vrdb/export?${params.toString()}`;
    }, 1500);
}

// 显示VRDB散点图
function showVrdbScatterPlot() {
    const chartContainer = document.getElementById('scatter-plot');
    
    // 显示加载状态
    showLoading('scatter-plot');
    
    // 模拟图表生成延迟
    setTimeout(() => {
        chartContainer.innerHTML = `
            <div style="text-align: center; width: 100%;">
                <h3>VRDB 数据散点图</h3>
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); height: 300px; display: flex; align-items: center; justify-content: center; color: white; border-radius: 8px; margin: 1rem 0;">
                    <div>
                        <i class="fas fa-chart-scatter fa-3x"></i>
                        <p style="margin-top: 1rem;">VRDB散点图可视化</p>
                        <p style="font-size: 0.9rem; opacity: 0.9;">电压-电流关系分析</p>
                    </div>
                </div>
                <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;">
                    <div>
                        <p style="font-weight: bold;">电压(V)</p>
                        <p>平均值: 3.95V</p>
                        <p>最大值: 5.0V</p>
                        <p>最小值: 3.0V</p>
                    </div>
                    <div>
                        <p style="font-weight: bold;">电流(A)</p>
                        <p>平均值: 0.65A</p>
                        <p>最大值: 0.8A</p>
                        <p>最小值: 0.5A</p>
                    </div>
                </div>
            </div>
        `;
    }, 1000);
}

// 查询TDDB数据
function searchTddbData() {
    const waferId = document.getElementById('tddb-wafer-id').value;
    const startDate = document.getElementById('tddb-start-date').value;
    const endDate = document.getElementById('tddb-end-date').value;
    
    // 显示加载状态
    showLoading('tddb-table');
    
    // 这里应该调用后端API获取数据
    console.log('查询TDDB数据:', { waferId, startDate, endDate });
    
    // 模拟API调用延迟
    setTimeout(() => {
        // 模拟数据
        const mockData = [
            { id: 1, wafer_id: 'WFR001', device_id: 'DEV001', voltage: 3.3, time: 1000, temperature: 125 },
            { id: 2, wafer_id: 'WFR002', device_id: 'DEV002', voltage: 5.0, time: 1500, temperature: 150 },
            { id: 3, wafer_id: 'WFR003', device_id: 'DEV003', voltage: 3.0, time: 800, temperature: 100 },
            { id: 4, wafer_id: 'WFR004', device_id: 'DEV004', voltage: 4.5, time: 1200, temperature: 135 }
        ];
        
        displayTddbTable(mockData);
    }, 1000);
}

// 显示TDDB数据表格
function displayTddbTable(data) {
    const tableContainer = document.getElementById('tddb-table');
    
    if (data.length === 0) {
        tableContainer.innerHTML = `
            <div style="text-align: center; padding: 2rem; color: #7f8c8d;">
                <i class="fas fa-info-circle fa-2x"></i>
                <p style="margin-top: 1rem;">未找到相关数据</p>
            </div>
        `;
        return;
    }
    
    let tableHtml = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Wafer ID</th>
                    <th>设备ID</th>
                    <th>电压(V)</th>
                    <th>时间(s)</th>
                    <th>温度(°C)</th>
                    <th>操作</th>
                </tr>
            </thead>
            <tbody>
    `;
    
    data.forEach(item => {
        tableHtml += `
            <tr>
                <td>${item.id}</td>
                <td>${item.wafer_id}</td>
                <td>${item.device_id}</td>
                <td>${item.voltage}</td>
                <td>${item.time}</td>
                <td>${item.temperature}</td>
                <td>
                    <button class="action-btn" onclick="viewTddbDetails(${item.id})">
                        <i class="fas fa-eye"></i> 查看详情
                    </button>
                </td>
            </tr>
        `;
    });
    
    tableHtml += `
            </tbody>
        </table>
    `;
    
    tableContainer.innerHTML = tableHtml;
}

// 导出TDDB数据
function exportTddbData() {
    // 获取查询条件
    const waferId = document.getElementById('tddb-wafer-id').value;
    const startDate = document.getElementById('tddb-start-date').value;
    const endDate = document.getElementById('tddb-end-date').value;
    
    // 显示加载状态
    const exportBtn = document.getElementById('export-tddb');
    const originalText = exportBtn.innerHTML;
    exportBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> 导出中...';
    exportBtn.disabled = true;
    
    // 构造请求参数
    const params = new URLSearchParams();
    if (waferId) params.append('wafer_id', waferId);
    if (startDate) params.append('start_date', startDate);
    if (endDate) params.append('end_date', endDate);
    
    // 模拟导出过程
    setTimeout(() => {
        // 恢复按钮状态
        exportBtn.innerHTML = originalText;
        exportBtn.disabled = false;
        
        // 显示成功消息
        alert('TDDB数据已成功导出!');
        
        // 这里应该实际调用后端导出接口
        // window.location.href = `/api/tddb/export?${params.toString()}`;
    }, 1500);
}

// 显示TDDB散点图
function showTddbScatterPlot() {
    const chartContainer = document.getElementById('tddb-scatter-plot');
    
    // 显示加载状态
    showLoading('tddb-scatter-plot');
    
    // 模拟图表生成延迟
    setTimeout(() => {
        chartContainer.innerHTML = `
            <div style="text-align: center; width: 100%;">
                <h3>TDDB 数据散点图</h3>
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); height: 300px; display: flex; align-items: center; justify-content: center; color: white; border-radius: 8px; margin: 1rem 0;">
                    <div>
                        <i class="fas fa-chart-scatter fa-3x"></i>
                        <p style="margin-top: 1rem;">TDDB散点图可视化</p>
                        <p style="font-size: 0.9rem; opacity: 0.9;">时间-电压关系分析</p>
                    </div>
                </div>
                <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;">
                    <div>
                        <p style="font-weight: bold;">电压(V)</p>
                        <p>平均值: 3.95V</p>
                        <p>最大值: 5.0V</p>
                        <p>最小值: 3.0V</p>
                    </div>
                    <div>
                        <p style="font-weight: bold;">时间(s)</p>
                        <p>平均值: 1125s</p>
                        <p>最大值: 1500s</p>
                        <p>最小值: 800s</p>
                    </div>
                </div>
            </div>
        `;
    }, 1000);
}

// 显示Wafer热力图
function showWaferHeatmap() {
    const chartContainer = document.getElementById('wafer-heatmap');
    
    // 显示加载状态
    showLoading('wafer-heatmap');
    
    // 模拟图表生成延迟
    setTimeout(() => {
        chartContainer.innerHTML = `
            <div style="text-align: center; width: 100%;">
                <h3>Wafer 热力图</h3>
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); height: 300px; display: flex; align-items: center; justify-content: center; color: white; border-radius: 8px; margin: 1rem 0;">
                    <div>
                        <i class="fas fa-th fa-3x"></i>
                        <p style="margin-top: 1rem;">Wafer热力图可视化</p>
                        <p style="font-size: 0.9rem; opacity: 0.9;">器件分布与性能分析</p>
                    </div>
                </div>
                <div style="margin-top: 1rem; text-align: left; max-width: 600px; margin: 1rem auto; padding: 1rem; background: #f8f9fa; border-radius: 8px;">
                    <h4><i class="fas fa-info-circle"></i> 热力图说明</h4>
                    <ul style="margin-top: 0.5rem; padding-left: 1.5rem;">
                        <li>颜色深浅表示器件性能指标</li>
                        <li>红色区域表示性能较差的器件</li>
                        <li>蓝色区域表示性能良好的器件</li>
                        <li>可通过坐标定位具体器件</li>
                    </ul>
                </div>
            </div>
        `;
    }, 1000);
}

// 生成报告
function generateReport() {
    const reportType = document.getElementById('reportType').value;
    const startDate = document.getElementById('reportStartDate').value;
    const endDate = document.getElementById('reportEndDate').value;
    
    // 验证输入
    if (!startDate || !endDate) {
        alert('请选择开始日期和结束日期');
        return;
    }
    
    // 显示加载状态
    showLoading('report-preview');
    
    // 获取下载按钮
    const downloadBtn = document.getElementById('download-report');
    
    // 禁用生成按钮，显示加载状态
    const generateBtn = document.getElementById('generate-report');
    const originalText = generateBtn.innerHTML;
    generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> 生成中...';
    generateBtn.disabled = true;
    
    // 模拟报告生成延迟
    setTimeout(() => {
        // 恢复生成按钮
        generateBtn.innerHTML = originalText;
        generateBtn.disabled = false;
        
        // 生成报告内容
        const reportContent = `
            <div style="padding: 1rem;">
                <h2 style="color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 0.5rem;">
                    <i class="fas fa-file-alt"></i> ${getReportTypeName(reportType)}
                </h2>
                <div style="margin: 1rem 0; padding: 1rem; background: #f8f9fa; border-radius: 8px;">
                    <p><strong>生成时间:</strong> ${new Date().toLocaleString('zh-CN')}</p>
                    <p><strong>报告类型:</strong> ${getReportTypeName(reportType)}</p>
                    <p><strong>统计周期:</strong> ${startDate} 至 ${endDate}</p>
                </div>
                <div style="margin: 1rem 0;">
                    <h3><i class="fas fa-chart-bar"></i> 数据概览</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
                        <div style="background: linear-gradient(135deg, #3498db, #2980b9); color: white; padding: 1rem; border-radius: 8px; text-align: center;">
                            <i class="fas fa-database fa-2x"></i>
                            <p style="margin-top: 0.5rem; font-size: 1.5rem; font-weight: bold;">1,250</p>
                            <p>数据记录</p>
                        </div>
                        <div style="background: linear-gradient(135deg, #2ecc71, #27ae60); color: white; padding: 1rem; border-radius: 8px; text-align: center;">
                            <i class="fas fa-check-circle fa-2x"></i>
                            <p style="margin-top: 0.5rem; font-size: 1.5rem; font-weight: bold;">98.5%</p>
                            <p>数据完整率</p>
                        </div>
                        <div style="background: linear-gradient(135deg, #e74c3c, #c0392b); color: white; padding: 1rem; border-radius: 8px; text-align: center;">
                            <i class="fas fa-exclamation-triangle fa-2x"></i>
                            <p style="margin-top: 0.5rem; font-size: 1.5rem; font-weight: bold;">12</p>
                            <p>异常记录</p>
                        </div>
                        <div style="background: linear-gradient(135deg, #f39c12, #d35400); color: white; padding: 1rem; border-radius: 8px; text-align: center;">
                            <i class="fas fa-tachometer-alt fa-2x"></i>
                            <p style="margin-top: 0.5rem; font-size: 1.5rem; font-weight: bold;">95.2%</p>
                            <p>性能达标率</p>
                        </div>
                    </div>
                </div>
                <div style="margin: 1rem 0;">
                    <h3><i class="fas fa-chart-line"></i> 趋势分析</h3>
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); height: 200px; display: flex; align-items: center; justify-content: center; color: white; border-radius: 8px; margin: 1rem 0;">
                        <div>
                            <i class="fas fa-chart-line fa-2x"></i>
                            <p style="margin-top: 1rem;">数据趋势图表</p>
                            <p style="font-size: 0.9rem; opacity: 0.9;">各项指标随时间变化趋势</p>
                        </div>
                    </div>
                </div>
                <div style="margin: 1rem 0;">
                    <h3><i class="fas fa-file-contract"></i> 结论与建议</h3>
                    <div style="padding: 1rem; background: #fff; border-left: 4px solid #3498db; margin-top: 1rem;">
                        <p>根据分析结果，制程可靠性整体表现良好，数据完整率达到98.5%，性能达标率为95.2%。建议继续监控关键参数，对识别出的12条异常记录进行深入分析。</p>
                    </div>
                </div>
            </div>
        `;
        
        // 显示报告内容
        document.getElementById('report-preview').innerHTML = reportContent;
        
        // 启用下载按钮
        downloadBtn.disabled = false;
        
        // 设置报告文件名
        document.getElementById('generatedReportFilename').value = `report_${reportType}_${new Date().getTime()}.pdf`;
    }, 2000);
}

// 获取报告类型名称
function getReportTypeName(type) {
    const types = {
        'comprehensive': '综合报告',
        'hci_nbti': 'HCI&NBTI报告',
        'vrdb': 'VRDB报告',
        'tddb': 'TDDB报告'
    };
    return types[type] || '未知报告';
}

// 下载报告
function downloadReport() {
    const filename = document.getElementById('generatedReportFilename').value;
    if (!filename) {
        alert('请先生成报告');
        return;
    }
    
    // 显示加载状态
    const downloadBtn = document.getElementById('download-report');
    const originalText = downloadBtn.innerHTML;
    downloadBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> 下载中...';
    downloadBtn.disabled = true;
    
    // 模拟下载延迟
    setTimeout(() => {
        // 恢复按钮状态
        downloadBtn.innerHTML = originalText;
        downloadBtn.disabled = false;
        
        // 显示成功消息
        alert(`报告 ${filename} 已成功下载!`);
        
        // 这里应该实际调用后端下载接口
        // window.location.href = `/api/reports/download/${filename}`;
    }, 1000);
}

// 查看详情（示例函数）
function viewDetails(id) {
    alert(`查看ID为 ${id} 的详细信息`);
    // 这里应该实现查看详情的逻辑
}

function viewVrdbDetails(id) {
    alert(`查看VRDB数据ID为 ${id} 的详细信息`);
    // 这里应该实现查看详情的逻辑
}

function viewTddbDetails(id) {
    alert(`查看TDDB数据ID为 ${id} 的详细信息`);
    // 这里应该实现查看详情的逻辑
}