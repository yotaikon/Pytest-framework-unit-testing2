def calculate_discount(price: float, discount_rate: float) -> float:
    """根据价格和折扣率计算折扣后的价格"""

    if not 0 < price < 10000:
        raise ValueError("Price must be between 0 and 10000")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1")
    
    return price * (1 - discount_rate)
