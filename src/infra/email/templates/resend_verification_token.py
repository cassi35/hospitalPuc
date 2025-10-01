from datetime import datetime
def resend_verification_token_template(token:int) -> str:
    response = f"""
    <!DOCTYPE html>
  <html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Verificação de E-mail</title>
  </head>
  <body style="margin:0; padding:0; background-color:#f4f4f4; font-family: Arial, sans-serif;">
    <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background-color:#f4f4f4; padding: 40px 0;">
      <tr>
        <td align="center">
          <table role="presentation" cellpadding="0" cellspacing="0" width="600" style="background:#ffffff; border-radius:12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <tr>
              <td style="background-color:#3b82f6; color:#ffffff; text-align:center; padding:20px; border-top-left-radius:12px; border-top-right-radius:12px;">
                <h2 style="margin:0;">hospital</h2>
              </td>
            </tr>
            <tr>
              <td style="padding: 30px 20px; text-align:center; color:#111827;">
                <h1 style="font-size:24px; margin-bottom:16px;">Verifique seu e-mail</h1>
                <p style="font-size:16px; color:#4b5563; margin-bottom:30px;">Use o código abaixo para concluir sua verificação de e-mail.</p>
                <div style="display:inline-block; background-color:#e0f2fe; color:#0284c7; padding:14px 24px; border-radius:8px; font-size:20px; letter-spacing:2px; font-weight:bold;">
                  {token}
                </div>
              </td>
            </tr>
            <tr>
              <td style="text-align:center; font-size:12px; color:#9ca3af; padding:20px; border-bottom-left-radius:12px; border-bottom-right-radius:12px;">
                © {datetime.now().year} hospital Todos os direitos reservados.
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
  </html>
"""
    return response