"""制程可靠性数据分析系统后端API
"""

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from backend.utils.database import get_db_session, init_database
from backend.models.hci_nbti_model import UnifiedHciNbtiData, CsvData
from backend.models.vrdb_model import VrdbData
from backend.models.tddb_model import TddbData
from backend.utils.report_generator import ReportGenerator
import os
from dotenv import load_dotenv
from config.config import APP_CONFIG, FILE_PATHS

# 加载环境变量
load_dotenv()

# 创建Flask应用
app = Flask(__name__)
CORS(app)  # 启用CORS

# 应用配置
app.config['SECRET_KEY'] = APP_CONFIG['secret_key']


@app.route('/')
def index():
    """首页
    """
    return jsonify({
        "message": "制程可靠性数据分析系统API",
        "status": "success"
    })


@app.route('/api/hci-nbti/search', methods=['GET'])
def search_hci_nbti():
    """查询HCI&NBTI数据
    """
    # 获取查询参数
    lot_id = request.args.get('lot_id', '')
    device_name = request.args.get('device_name', '')
    
    # 获取数据库会话
    session = get_db_session()
    
    try:
        # 构建查询
        query = session.query(UnifiedHciNbtiData)
        
        if lot_id:
            query = query.filter(UnifiedHciNbtiData.lot_id.like(f'%{lot_id}%'))
            
        if device_name:
            query = query.filter(UnifiedHciNbtiData.device_name.like(f'%{device_name}%'))
            
        # 执行查询
        results = query.all()
        
        # 转换为字典列表
        data = [{
            'id': item.id,
            'lot_id': item.lot_id,
            'device_id': item.device_id,
            'device_name': item.device_name,
            'std': item.std,
            'vtd': item.vtd,
            'csv_name': item.csv_name
        } for item in results]
        
        return jsonify({
            "status": "success",
            "data": data,
            "count": len(data)
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    finally:
        session.close()


@app.route('/api/hci-nbti/export', methods=['GET'])
def export_hci_nbti():
    """导出HCI&NBTI数据为Excel
    """
    # 这里应该实现数据导出逻辑
    # 暂时返回一个模拟的文件路径
    return jsonify({
        "status": "success",
        "message": "HCI&NBTI数据已导出",
        "file_path": "/exports/hci_nbti_data.xlsx"
    })


@app.route('/api/vrdb/search', methods=['GET'])
def search_vrdb():
    """查询VRDB数据
    """
    # 获取查询参数
    device_id = request.args.get('device_id', '')
    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    
    # 获取数据库会话
    session = get_db_session()
    
    try:
        # 构建查询
        query = session.query(VrdbData)
        
        if device_id:
            query = query.filter(VrdbData.device_id.like(f'%{device_id}%'))
            
        # 这里应该添加日期范围的过滤逻辑
        
        # 执行查询
        results = query.all()
        
        # 转换为字典列表
        data = [{
            'id': item.id,
            'device_id': item.device_id,
            'test_date': item.test_date.isoformat() if item.test_date else None,
            'voltage': item.voltage,
            'current': item.current,
            'resistance': item.resistance,
            'temperature': item.temperature
        } for item in results]
        
        return jsonify({
            "status": "success",
            "data": data,
            "count": len(data)
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    finally:
        session.close()


@app.route('/api/vrdb/export', methods=['GET'])
def export_vrdb():
    """导出VRDB数据
    """
    # 这里应该实现数据导出逻辑
    return jsonify({
        "status": "success",
        "message": "VRDB数据已导出"
    })


@app.route('/api/tddb/search', methods=['GET'])
def search_tddb():
    """查询TDDB数据
    """
    # 获取查询参数
    wafer_id = request.args.get('wafer_id', '')
    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    
    # 获取数据库会话
    session = get_db_session()
    
    try:
        # 构建查询
        query = session.query(TddbData)
        
        if wafer_id:
            query = query.filter(TddbData.wafer_id.like(f'%{wafer_id}%'))
            
        # 这里应该添加日期范围的过滤逻辑
        
        # 执行查询
        results = query.all()
        
        # 转换为字典列表
        data = [{
            'id': item.id,
            'device_id': item.device_id,
            'wafer_id': item.wafer_id,
            'x_coordinate': item.x_coordinate,
            'y_coordinate': item.y_coordinate,
            'value': item.value,
            'test_date': item.test_date.isoformat() if item.test_date else None
        } for item in results]
        
        return jsonify({
            "status": "success",
            "data": data,
            "count": len(data)
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    finally:
        session.close()


@app.route('/api/tddb/export', methods=['GET'])
def export_tddb():
    """导出TDDB数据
    """
    # 这里应该实现数据导出逻辑
    return jsonify({
        "status": "success",
        "message": "TDDB数据已导出"
    })


@app.route('/api/report/generate', methods=['POST'])
def generate_report():
    """生成综合分析报告
    """
    try:
        # 获取请求参数
        data = request.json
        report_type = data.get('type', 'comprehensive')  # hci_nbti, vrdb, tddb, comprehensive
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        # 创建报告生成器
        report_generator = ReportGenerator()
        
        # 根据报告类型生成相应报告
        if report_type == 'hci_nbti':
            # 查询HCI&NBTI数据
            session = get_db_session()
            query = session.query(UnifiedHciNbtiData)
            if start_date and end_date:
                query = query.filter(UnifiedHciNbtiData.test_date >= start_date, UnifiedHciNbtiData.test_date <= end_date)
            hci_nbti_data = [{'id': item.id, 'lot_id': item.lot_id, 'device_id': item.device_id, 
                            'device_name': item.device_name, 'std': item.std, 'vtd': item.vtd,
                            'test_date': item.test_date.strftime('%Y-%m-%d') if item.test_date else ''}
                           for item in query.all()]
            session.close()
            
            # 生成报告
            file_path = report_generator.generate_hci_nbti_report(hci_nbti_data, start_date, end_date)
            filename = os.path.basename(file_path)
            return jsonify({'success': True, 'filename': filename})
            
        elif report_type == 'vrdb':
            # 查询VRDB数据
            session = get_db_session()
            query = session.query(VrdbData)
            if start_date and end_date:
                query = query.filter(VrdbData.test_date >= start_date, VrdbData.test_date <= end_date)
            vrdb_data = [{'id': item.id, 'device_id': item.device_id, 'test_date': item.test_date.strftime('%Y-%m-%d'),
                         'voltage': item.voltage, 'current': item.current, 'resistance': item.resistance}
                        for item in query.all()]
            session.close()
            
            # 生成报告
            file_path = report_generator.generate_vrdb_report(vrdb_data, start_date, end_date)
            filename = os.path.basename(file_path)
            return jsonify({'success': True, 'filename': filename})
            
        elif report_type == 'tddb':
            # 查询TDDB数据
            session = get_db_session()
            query = session.query(TddbData)
            if start_date and end_date:
                query = query.filter(TddbData.test_date >= start_date, TddbData.test_date <= end_date)
            tddb_data = [{'id': item.id, 'device_id': item.device_id, 'wafer_id': item.wafer_id,
                         'x_coordinate': item.x_coordinate, 'y_coordinate': item.y_coordinate, 'value': item.value,
                         'test_date': item.test_date.strftime('%Y-%m-%d')}
                        for item in query.all()]
            session.close()
            
            # 生成报告
            file_path = report_generator.generate_tddb_report(tddb_data, start_date, end_date)
            filename = os.path.basename(file_path)
            return jsonify({'success': True, 'filename': filename})
            
        else:  # comprehensive
            # 查询所有数据
            session = get_db_session()
            
            # 查询HCI&NBTI数据
            hci_nbti_query = session.query(UnifiedHciNbtiData)
            if start_date and end_date:
                hci_nbti_query = hci_nbti_query.filter(UnifiedHciNbtiData.test_date >= start_date, UnifiedHciNbtiData.test_date <= end_date)
            hci_nbti_data = [{'id': item.id, 'lot_id': item.lot_id, 'device_id': item.device_id, 
                            'device_name': item.device_name, 'std': item.std, 'vtd': item.vtd}
                           for item in hci_nbti_query.all()]
            
            # 查询VRDB数据
            vrdb_query = session.query(VrdbData)
            if start_date and end_date:
                vrdb_query = vrdb_query.filter(VrdbData.test_date >= start_date, VrdbData.test_date <= end_date)
            vrdb_data = [{'id': item.id, 'device_id': item.device_id, 'test_date': item.test_date.strftime('%Y-%m-%d'),
                         'voltage': item.voltage, 'current': item.current, 'resistance': item.resistance}
                        for item in vrdb_query.all()]
            
            # 查询TDDB数据
            tddb_query = session.query(TddbData)
            if start_date and end_date:
                tddb_query = tddb_query.filter(TddbData.test_date >= start_date, TddbData.test_date <= end_date)
            tddb_data = [{'id': item.id, 'device_id': item.device_id, 'wafer_id': item.wafer_id,
                         'x_coordinate': item.x_coordinate, 'y_coordinate': item.y_coordinate, 'value': item.value}
                        for item in tddb_query.all()]
            
            session.close()
            
            # 生成报告
            file_path = report_generator.generate_comprehensive_report(hci_nbti_data, vrdb_data, tddb_data, start_date, end_date)
            filename = os.path.basename(file_path)
            return jsonify({'success': True, 'filename': filename})
            
    except Exception as e:
        return jsonify({'error': f'生成报告时出错: {str(e)}'}), 500


@app.route('/api/report/download/<filename>')
def download_report(filename):
    """下载生成的报告
    """
    try:
        return send_file(os.path.join(FILE_PATHS['reports'], filename), as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': '报告文件不存在'}), 404
    except Exception as e:
        return jsonify({'error': f'下载报告时出错: {str(e)}'}), 500


if __name__ == '__main__':
    init_database()
    app.run(host=APP_CONFIG['host'], port=APP_CONFIG['port'], debug=APP_CONFIG['debug'])