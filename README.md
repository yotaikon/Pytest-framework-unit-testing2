# 折扣计算器单元测试

这个项目包含了一个折扣计算函数的完整单元测试套件。

## 提示词

```bash
@discount_calculator.py  你是一位资深的Python测试工程师。
请为以下  \`calculate_discount\` 函数编写单元测试：
1. 使用  \`pytest\` 框架。
2. 全面覆盖正常场景、所有边界条件和  \`ValueError\` 异常场景。
3. 为每个测试用例起一个清晰的、能反映其意图的名字。
```

## 项目结构

- `discount_calculator.py` - 包含 `calculate_discount` 函数的实现
- `test_discount_calculator.py` - 完整的单元测试套件
- `requirements.txt` - 项目依赖
- `README.md` - 项目说明文档

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行测试

在项目根目录下运行：

```bash
pytest test_discount_calculator.py -v
```

或者运行所有测试：

```bash
pytest -v
```

## 测试覆盖范围

测试套件覆盖了以下场景：

### 正常场景测试
- 标准折扣计算
- 无折扣（折扣率为0）
- 全额折扣（折扣率为1）
- 小数折扣率

### 边界条件测试
- 最小有效价格（接近0）
- 最大有效价格（接近10000）
- 最小折扣率（0）
- 最大折扣率（1）
- 接近边界的值

### 异常场景测试
- 价格为0或负数
- 价格达到或超过10000
- 折扣率为负数
- 折扣率超过1

### 精度测试
- 浮点数计算精度
- 边界值的精确计算

## 函数说明

`calculate_discount(price: float, discount_rate: float) -> float`

- **参数**：
  - `price`: 商品价格，必须在 (0, 10000) 范围内
  - `discount_rate`: 折扣率，必须在 [0, 1] 范围内
- **返回值**：折扣后的价格
- **异常**：当参数超出有效范围时抛出 `ValueError`
