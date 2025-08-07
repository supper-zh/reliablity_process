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
});

// 查询HCI&NBTI数据
function searchHciNbtiData() {
    const lotId = document.getElementById('lot-id').value;
    const deviceName = document.getElementById('device-name').value;
    
    // 这里应该调用后端API获取数据
    console.log('查询HCI&NBTI数据:', { lotId, deviceName });
    
    // 模拟数据
    const mockData = [
        { id: 1, lot_id: 'LOT001', device_id: 'DEV001', device_name: 'Device A', std: 'STD001', vtd: 1.23 },
        { id: 2, lot_id: 'LOT002', device_id: 'DEV002', device_name: 'Device B', std: 'STD002', vtd: 2.34 }
    ];
    
    displayHciNbtiTable(mockData);
}

// 显示HCI&NBTI数据表格
function displayHciNbtiTable(data) {
    const tableContainer = document.getElementById('hci-nbti-table');
    
    if (data.length === 0) {
        tableContainer.innerHTML = '<p>未找到相关数据</p>';
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
    const lotId = document.getElementById('hci-nbti-lot-id').value;
    const deviceId = document.getElementById('hci-nbti-device-id').value;
    const startDate = document.getElementById('hci-nbti-start-date').value;
    const endDate = document.getElementById('hci-nbti-end-date').value;
    
    // 构造请求参数
    const params = new URLSearchParams();
    if (lotId) params.append('lot_id', lotId);
    if (deviceId) params.append('device_id', deviceId);
    if (startDate) params.append('start_date', startDate);
    if (endDate) params.append('end_date', endDate);
    
    // 请求后端导出数据
    window.location.href = `/api/hci-nbti/export?${params.toString()}`;
}

// 查询VRDB数据
function searchVrdbData() {
    const deviceId = document.getElementById('vrdb-device-id').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    
    // 这里应该调用后端API获取数据
    console.log('查询VRDB数据:', { deviceId, startDate, endDate });
    
    // 模拟数据
    const mockData = [
        { id: 1, device_id: 'DEV001', voltage: 3.3, current: 0.5, resistance: 6.6 },
        { id: 2, device_id: 'DEV002', voltage: 5.0, current: 0.8, resistance: 6.25 }
    ];
    
    displayVrdbTable(mockData);
}

// 显示VRDB数据表格
function displayVrdbTable(data) {
    const tableContainer = document.getElementById('vrdb-table');
    
    if (data.length === 0) {
        tableContainer.innerHTML = '<p>未找到相关数据</p>';
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
    const startDate = document.getElementById('vrdb-start-date').value;
    const endDate = document.getElementById('vrdb-end-date').value;
    
    // 构造请求参数
    const params = new URLSearchParams();
    if (deviceId) params.append('device_id', deviceId);
    if (startDate) params.append('start_date', startDate);
    if (endDate) params.append('end_date', endDate);
    
    // 请求后端导出数据
    window.location.href = `/api/vrdb/export?${params.toString()}`;
}

// 显示VRDB散点图
function showVrdbScatterPlot() {
    // 从后端获取VRDB数据
    fetch('/api/vrdb/search')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const chartContainer = document.getElementById('scatter-plot');
                chartContainer.innerHTML = '<p>VRDB散点图显示区域</p><canvas id="vrdb-scatter-chart"></canvas>';
                
                // 这里应该使用Chart.js或其他图表库绘制散点图
                console.log('显示VRDB散点图:', data.data);
                alert('VRDB散点图显示完成！');
            } else {
                alert('获取VRDB数据失败: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('获取VRDB数据失败: ' + error.message);
        });
}

// 查询TDDB数据
function searchTddbData() {
    const waferId = document.getElementById('tddb-wafer-id').value;
    const startDate = document.getElementById('tddb-start-date').value;
    const endDate = document.getElementById('tddb-end-date').value;
    
    // 这里应该调用后端API获取数据
    console.log('查询TDDB数据:', { waferId, startDate, endDate });
    
    // 模拟数据
    const mockData = [
        { id: 1, device_id: 'DEV001', wafer_id: 'WFR001', x: 10, y: 20, value: 1.23 },
        { id: 2, device_id: 'DEV001', wafer_id: 'WFR001', x: 15, y: 25, value: 2.34 }
    ];
    
    displayTddbTable(mockData);
}

// 显示TDDB数据表格
function displayTddbTable(data) {
    const tableContainer = document.getElementById('tddb-table');
    
    if (data.length === 0) {
        tableContainer.innerHTML = '<p>未找到相关数据</p>';
        return;
    }
    
    let tableHtml = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>设备ID</th>
                    <th>Wafer ID</th>
                    <th>X坐标</th>
                    <th>Y坐标</th>
                    <th>数值</th>
                </tr>
            </thead>
            <tbody>
    `;
    
    data.forEach(item => {
        tableHtml += `
            <tr>
                <td>${item.id}</td>
                <td>${item.device_id}</td>
                <td>${item.wafer_id}</td>
                <td>${item.x}</td>
                <td>${item.y}</td>
                <td>${item.value}</td>
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
    
    // 构造请求参数
    const params = new URLSearchParams();
    if (waferId) params.append('wafer_id', waferId);
    if (startDate) params.append('start_date', startDate);
    if (endDate) params.append('end_date', endDate);
    
    // 请求后端导出数据
    window.location.href = `/api/tddb/export?${params.toString()}`;
}

// 显示TDDB散点图
function showTddbScatterPlot() {
    // 从后端获取TDDB数据
    fetch('/api/tddb/search')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const chartContainer = document.getElementById('tddb-scatter-plot');
                chartContainer.innerHTML = '<p>TDDB散点图显示区域</p><canvas id="tddb-scatter-chart"></canvas>';
                
                // 这里应该使用Chart.js或其他图表库绘制散点图
                console.log('显示TDDB散点图:', data.data);
                alert('TDDB散点图显示完成！');
            } else {
                alert('获取TDDB数据失败: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('获取TDDB数据失败: ' + error.message);
        });
}

// 显示Wafer热力图
function showWaferHeatmap() {
    // 从后端获取TDDB数据
    fetch('/api/tddb/search')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const chartContainer = document.getElementById('wafer-heatmap');
                chartContainer.innerHTML = '<p>Wafer热力图显示区域</p><canvas id="wafer-heatmap-chart"></canvas>';
                
                // 这里应该使用D3.js或其他图表库绘制热力图
                console.log('显示Wafer热力图:', data.data);
                alert('Wafer热力图显示完成！');
            } else {
                alert('获取TDDB数据失败: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('获取TDDB数据失败: ' + error.message);
        });
}

// 生成报告
function generateReport() {
    // 获取选择的报告类型
    const reportType = document.getElementById('reportType').value;
    
    // 获取日期范围
    const startDate = document.getElementById('reportStartDate').value;
    const endDate = document.getElementById('reportEndDate').value;
    
    // 构造请求数据
    const requestData = {
        type: reportType,
        start_date: startDate,
        end_date: endDate
    };
    
    // 发送请求生成报告
    fetch('/api/report/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(`报告生成成功: ${data.filename}`);
            // 保存文件名用于下载
            document.getElementById('generatedReportFilename').value = data.filename;
        } else {
            alert(`报告生成失败: ${data.error}`);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('报告生成失败: ' + error.message);
    });
}

// 报告下载
function downloadReport() {
    // 获取生成的报告文件名
    const filename = document.getElementById('generatedReportFilename').value;
    
    if (!filename) {
        alert('请先生成报告');
        return;
    }
    
    // 下载报告
    window.open(`/api/report/download/${filename}`, '_blank');
}