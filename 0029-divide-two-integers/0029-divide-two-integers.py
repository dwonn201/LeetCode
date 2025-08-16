class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # 32비트 정수 범위 상수 정의
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        # 1. 부호 결정
        is_negative = (dividend < 0) != (divisor < 0)

        # 2. 절댓값 변환
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        # 3. 비트 시프트 기반의 효율적인 반복 뺄셈
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            
            # temp_divisor를 2배씩 늘려가며 dividend에서 뺄 수 있는지 확인
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # 뺄 수 있는 가장 큰 값을 찾았으므로 빼고 몫에 더하기
            abs_dividend -= temp_divisor
            quotient += multiple
        
        # 4. 부호 적용 및 오버플로우 처리
        if is_negative:
            quotient = -quotient
            
        if quotient < MIN_INT:
            return MIN_INT
        elif quotient > MAX_INT:
            return MAX_INT
        else:
            return quotient