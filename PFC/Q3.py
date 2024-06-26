def withdraw_amount_policy(total_balance, min_balance_limit, withdraw_amount):
    if total_balance - withdraw_amount < min_balance_limit:
        return f"Your balance is {total_balance} and you are unable to withdraw {withdraw_amount} as your balance cannot be less than {min_balance_limit}."
    else:
        remaining_balance = total_balance - withdraw_amount
        return f"Thank you for using our services. Your balance is {remaining_balance}."