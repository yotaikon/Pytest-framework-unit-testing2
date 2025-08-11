import pytest
from discount_calculator import calculate_discount


class TestCalculateDiscount:
    """测试calculate_discount函数的各种场景"""
    
    def test_normal_discount_calculation(self):
        """测试正常的折扣计算场景"""
        # 测试标准折扣场景
        assert calculate_discount(100.0, 0.2) == 80.0
        assert calculate_discount(50.0, 0.5) == 25.0
        assert calculate_discount(200.0, 0.1) == 180.0
    
    def test_no_discount(self):
        """测试无折扣场景（折扣率为0）"""
        assert calculate_discount(100.0, 0.0) == 100.0
        assert calculate_discount(500.0, 0.0) == 500.0
    
    def test_full_discount(self):
        """测试全额折扣场景（折扣率为1）"""
        assert calculate_discount(100.0, 1.0) == 0.0
        assert calculate_discount(75.0, 1.0) == 0.0
    
    def test_decimal_discount_rates(self):
        """测试小数折扣率场景"""
        assert calculate_discount(100.0, 0.25) == 75.0
        assert calculate_discount(100.0, 0.33) == 67.0
        assert calculate_discount(100.0, 0.75) == 25.0
    
    def test_boundary_price_values(self):
        """测试边界价格值"""
        # 测试最小有效价格（接近0但不等于0）
        assert calculate_discount(0.01, 0.1) == pytest.approx(0.009, rel=1e-10)
        
        # 测试最大有效价格（接近10000但不等于10000）
        assert calculate_discount(9999.99, 0.2) == pytest.approx(7999.992, rel=1e-10)
    
    def test_boundary_discount_rate_values(self):
        """测试边界折扣率值"""
        # 测试最小折扣率
        assert calculate_discount(100.0, 0.0) == 100.0
        
        # 测试最大折扣率
        assert calculate_discount(100.0, 1.0) == 0.0
        
        # 测试接近0的折扣率
        assert calculate_discount(100.0, 0.001) == pytest.approx(99.9, rel=1e-10)
        
        # 测试接近1的折扣率
        assert calculate_discount(100.0, 0.999) == pytest.approx(0.1, rel=1e-10)
    
    def test_float_precision(self):
        """测试浮点数精度"""
        # 33.33 * (1 - 0.33) = 33.33 * 0.67 = 22.3311
        assert calculate_discount(33.33, 0.33) == pytest.approx(22.3311, rel=1e-10)
        # 99.99 * (1 - 0.25) = 99.99 * 0.75 = 74.9925
        assert calculate_discount(99.99, 0.25) == pytest.approx(74.9925, rel=1e-10)
    
    def test_price_zero_raises_value_error(self):
        """测试价格为0时抛出ValueError异常"""
        with pytest.raises(ValueError, match="Price must be between 0 and 10000"):
            calculate_discount(0.0, 0.2)
    
    def test_price_negative_raises_value_error(self):
        """测试价格为负数时抛出ValueError异常"""
        with pytest.raises(ValueError, match="Price must be between 0 and 10000"):
            calculate_discount(-10.0, 0.2)
    
    def test_price_maximum_raises_value_error(self):
        """测试价格为10000时抛出ValueError异常"""
        with pytest.raises(ValueError, match="Price must be between 0 and 10000"):
            calculate_discount(10000.0, 0.2)
    
    def test_price_above_maximum_raises_value_error(self):
        """测试价格超过10000时抛出ValueError异常"""
        with pytest.raises(ValueError, match="Price must be between 0 and 10000"):
            calculate_discount(10001.0, 0.2)
    
    def test_discount_rate_negative_raises_value_error(self):
        """测试折扣率为负数时抛出ValueError异常"""
        with pytest.raises(ValueError, match="Discount rate must be between 0 and 1"):
            calculate_discount(100.0, -0.1)
    
    def test_discount_rate_above_one_raises_value_error(self):
        """测试折扣率超过1时抛出ValueError异常"""
        with pytest.raises(ValueError, match="Discount rate must be between 0 and 1"):
            calculate_discount(100.0, 1.1)
    
    def test_discount_rate_below_zero_raises_value_error(self):
        """测试折扣率小于0时抛出ValueError异常"""
        with pytest.raises(ValueError, match="Discount rate must be between 0 and 1"):
            calculate_discount(100.0, -0.5)
    
    def test_discount_rate_well_above_one_raises_value_error(self):
        """测试折扣率远大于1时抛出ValueError异常"""
        with pytest.raises(ValueError, match="Discount rate must be between 0 and 1"):
            calculate_discount(100.0, 1.5)
    
    def test_edge_case_very_small_price(self):
        """测试极小价格边界情况"""
        # 测试接近0但不等于0的价格
        assert calculate_discount(0.001, 0.5) == pytest.approx(0.0005, rel=1e-10)
    
    def test_edge_case_very_large_price(self):
        """测试极大价格边界情况"""
        # 测试接近10000但不等于10000的价格
        assert calculate_discount(9999.999, 0.1) == pytest.approx(8999.9991, rel=1e-10)
    
    def test_edge_case_very_small_discount_rate(self):
        """测试极小折扣率边界情况"""
        # 测试接近0但不等于0的折扣率
        assert calculate_discount(100.0, 0.0001) == pytest.approx(99.99, rel=1e-10)
    
    def test_edge_case_very_large_discount_rate(self):
        """测试极大折扣率边界情况"""
        # 测试接近1但不等于1的折扣率
        assert calculate_discount(100.0, 0.9999) == pytest.approx(0.01, rel=1e-10)
