from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.ProjectConfig import ETConfig
from common.logger import write_log
import smtplib
import time
class sendEmail:

    # 发送邮件函数
    def send_mail(self):

        """
        发送邮件
        :return:
        """
        # 打开报告文件
        # 邮箱信息
        self.smtpserver = ETConfig.EMAIL_CONFIG['EMAIL_SERVER']
        self.user = ETConfig.EMAIL_CONFIG['EMAIL_USER']
        self.password = ETConfig.EMAIL_CONFIG['EMAIL_PWD']
        self.sender = ETConfig.EMAIL_CONFIG['EMAIL_SENDER']
        self.receiver = ETConfig.EMAIL_CONFIG['EMAIL_RECEIVER']
        self.report_dir=ETConfig.Report_DIR
        # # html报告路径
        # self.report_dir = "{}report".format((ETConfig.Report_DIR))
        with open('{}\\et_result.html'.format(self.report_dir), 'rb') as f:
            mail_body = str(f.read(), encoding="utf-8")

        msg = MIMEMultipart('mixed')
        msg_html = MIMEText(mail_body, 'html', 'utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)
        msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(msg_html1)#附件

        msg['Subject'] = u'自动化测试报告 {}'.format(time.strftime("%Y-%m-%d", time.localtime()))
        msg['From'] = u'AutoTest <%s>' % self.sender
        msg['To'] = self.receiver
        # msg['Cc'] = self.cc

        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.user, self.password)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())
            smtp.quit()
            write_log.info("发送邮件成功！")
        except Exception as e:
            write_log.error("发送邮件失败：{}".format(e))