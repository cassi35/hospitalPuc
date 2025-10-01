from src.domain.models.user_email import UserEmail
def send_welcome_email_template(user_email: UserEmail) -> str:
    response = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Our Service!</title>
</head>
<body>
    <h1>Welcome, {user_email.name}!</h1>
    <p>Thank you for joining us. We are excited to have you on board!</p>
    <p>If you have any questions, feel free to reach out to our support team.</p>
    <p>Best regards,<br>Your Company Team</p>
</body>
</html>
"""
    return response