from PyQt5 import QtCore

user_info = {
    'first_name': None,
    'last_name': None,
    'user_client_id':None, 
}

transaction_info = { 
    'transaction_id': None,
    'reference_number': None
}

class Config:
    DEFAULT_LANGUAGE = "English"
    current_language = DEFAULT_LANGUAGE
    language_changed = QtCore.pyqtSignal(str)

    @classmethod
    def set_language(cls, language):
        cls.current_language = language

    predicted_class = None

    @classmethod
    def set_predicted_class(cls, predicted_class):
        cls.predicted_class = predicted_class
        print(f"Predicted class set in Config: {predicted_class}")

translations = {
    'English': {
        # Index Page
        'MainWindow_Title': 'MainWindow',
        'StartShopping_Button': 'Start Shopping',
        'ProductLabel_Text': 'IM.AI Cart',
        'CompanyLabel_Text': '<html><head/><body><p><span style="font-size:12pt;">Powered by </span><span style="font-size:12pt; font-weight:600;">Linoflap Technologies Philippines Inc.</span></p></body></html>',
        'ComboBox_English': 'English',
        'ComboBox_Japanese': '日本語',
        'Welcome_Title': 'Welcome!',
        'Welcome_Message': 'Making your shopping convenient and hassle-free.',
        # Login Option
        'Welcome': 'Are you already a member?',
        'Member': 'Yes, I am a member',
        'Non_Member': 'No, I am not a member',
        # Login Member
        'Welcome_Label': 'Welcome Shopper!',
        'Secondary_Label': 'Good to see you!',
        'Email_Label': 'E-Mail:',
        'Password_Label': 'Password',
        'Login_Button': 'Login',
        'Back_Button': 'Back',
        'QR_Label': 'Log in with QR Code',
        'Scan_Label': '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Scan this with the Supermarket </span></p></body></html>',
        'Scan_Label_2': '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">mobile app to log in instantly.</span></p></body></html>',
        'Invalid_Login_Message': 'Invalid username or password.',
        'Invalid_Login_Title': 'Login Failed',
        'Input_Required_Message': 'Please enter username and password.',
        'Input_Required_Title': 'Input Required',
        # Login Member Tutorial
        'Skip_Button': 'Skip',
        'Next_Button': 'Next',
        # Item View, Card, Cash, eWallet Payment Option
        'Welcome_User': 'Welcome',
        'Role_Output': 'Member',
        'Help_Button': 'Help',
        'Shopping_List_Button': 'Shopping List',
        'Search_Products_Button': 'Search Products',
        'Product_Label': 'Product',
        'Detail_Label': 'Details',
        'Price_Label': 'Price',
        'Barcode_Label': 'Barcode',
        'Summary_Label': 'Summary',
        'Remove_Label': 'Remove Item',
        'Total_Products_Label': 'Number of Products',
        'Total_Items_Label': 'Number of Items',
        'Total_Price_Label': 'Total Price',
        'Total_Products_Output': '0 products',
        'Discount_Label':'Discount', 
        'Discount_Output':'¥ 0.00',
        'Discount_Name':'10% OFF',
        'Total_Items_Output': '0 Items',
        'Total_Price_Output': '¥ 0.00',
        'Checkout_Button': 'Proceed to Checkout',
        'Payment_Button': 'Proceed to Payment',
        'Scan_Barcode_Push_Button': 'Open Barcode Scanner',
        # Item View Error Message
        'Close_Barcode_Scanner': 'Close Barcode Scanner',
        'Scan_Barcode_Title': 'Scan Barcode',
        'Scan_Barcode_Message': 'Please position the barcode in front of the camera. Click again the button to close the scanner.',
        'Open_Barcode_Scanner': 'Open Barcode Scanner',
        'Scanning_Done_Title': 'Scanning Done',
        'Scanning_Done_Message': 'Barcode scanning is complete.',
        'Scanner_Closed_Title': 'Scanner Closed',
        'Scanner_Closed_Message': 'No scans for 30 seconds. Barcode scanner closed.',
        'Add_Remove_Title':'Shopping Paused!',
        'Add_Before_Scan_Message': 'Remove the added item to continue shopping!',
        'Remove_Before_Scan_Message': 'Scan it to remove the item or put it back in the cart to continue.',
        'Put_Item_Message': 'Place the scanned item inside the cart',
        'Put_Item_Error_Message': 'Please rescan the item as it wasn\'t put in after 10 seconds.',
        # Payment Option 
        'Payment_Label': 'Choose Payment Method',
        'Card_Label': '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Card Payment</span></p></body></html>',
        'E_Wallet_Label': '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">E-Wallet Payment</span></p></body></html>',
        'Cash_Label': '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cash Payment</span></p></body></html>',
        'Card_Payment': 'Card Payment',
        'E_Wallet_Payment': 'E-Wallet Payment',
        'Cash_Payment': 'Cash Payment',
        'Voucher_Label': 'Vouchers Available',
        # Feedback 
        'Finish_Push_Button': 'Finish Shopping',
        'Feedback_Push_Button': 'Give Feedback',
        'Thankyou_Label': 'Thank you Dear Shopper!',
        'Feedback_Paragraph': '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style="font-family:'Montserrat'; font-size:20px; font-weight:400; font-style:normal;">
<p align="center" style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-family:'MS Shell Dlg 2'; font-size:16pt;">We value your experience! Share your thoughts on your </span></p>
<p align="center" style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-family:'MS Shell Dlg 2'; font-size:16pt;">recent </span><span style="font-family:'MS Shell Dlg 2'; font-size:16pt; font-weight:600;">IM.AI Cart</span><span style="font-family:'MS Shell Dlg 2'; font-size:16pt;"> journey to help us enhance our services. </span></p>
<p align="center" style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-family:'MS Shell Dlg 2'; font-size:16pt;">Your feedback is invaluable to us. </span></p></body></html>''',
        # Search 
        'Search_Line_Edit': 'Search Products...',
        # Feedback Questions
        'Finish_Button': 'Finish Shopping',
        'Question_1': 'How would you rate your overall experience using our Smart Shopping Cart?',
        'Q1_Answer_1': 'Excellent',
        'Q1_Answer_2': 'Very Poor',
        'Q1_Answer_3': 'Good',
        'Q1_Answer_4': 'Poor',
        'Q1_Answer_5': 'Neutral',
        'Question_2': 'How user-friendly did you find the Smart Shopping Cart interface',
        'Q2_Answer_1': 'Extremely user-friendly',
        'Q2_Answer_2': 'Not at all user-friendly',
        'Q2_Answer_3': 'Very user-friendly',
        'Q2_Answer_4': 'Slightly user-friendly',
        'Q2_Answer_5': 'Moderately user-friendly',
        'Question_3': 'How satisfied were you with the accuracy of product recognition by the Smart Cart?',
        'Q3_Answer_1': 'No',
        'Q3_Answer_2': 'Yes',
        'Question_4': 'Did the Smart Cart enhance the efficiency of your shopping experience?',
        'Q4_Answer_1': 'Very Satisfied',
        'Q4_Answer_2': 'Dissatisfied',
        'Q4_Answer_3': 'Very Dissatisfied',
        'Q4_Answer_4': 'Satisfied',
        'Q4_Answer_5': 'Neutral',
        'Question_5': 'How likely are you to recommend the Smart Shopping Cart to a friend or family member?',
        'Q5_Answer_1': 'Extremely likely',
        'Q5_Answer_2': 'Neutral',
        'Q5_Answer_3': 'Slightly likely',
        'Q5_Answer_4': 'Not likely at all',
        'Q5_Answer_5': 'Very likely',
    },
    '日本語': {
        # Index Page
        'MainWindow_Title': 'メインウィンドウ',
        'StartShopping_Button': 'ショッピングを開始',
        'ProductLabel_Text': 'IM.AI カート',
        'CompanyLabel_Text': '<html><head/><body><p><span style="font-size:12pt;">提供元 </span><span style="font-size:12pt; font-weight:600;">Linoflap Technologies Philippines Inc.</span></p></body></html>',
        'ComboBox_English': 'English',
        'ComboBox_Japanese': '日本語',
        'Welcome_Title': 'ようこそ！',
        'Welcome_Message': 'お買い物を便利でストレスフリーにするために。',
        # Login Option
        'Welcome': 'ようこそ！もうメンバーですか？',
        'Member': 'はい、メンバーです。',
        'Non_Member': 'いいえ、メンバーではありません。',
        # Login Member
        'Welcome_Label': 'ようこそ、ショッパーさん！',
        'Secondary_Label': 'お会いできて嬉しいです！',
        'Email_Label': 'メール:',
        'Password_Label': 'パスワード',
        'Login_Button': 'ログイン',
        'Back_Button': '戻る',
        'QR_Label': 'QRコードでログイン',
        'Scan_Label': '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">これをスーパーマーケットのアプリでスキャンしてください </span></p></body></html>',
        'Scan_Label_2': '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">瞬時にログインできます。</span></p></body></html>',
        'Invalid_Login_Message': 'ユーザー名またはパスワードが無効です。',
        'Invalid_Login_Title': 'ログイン失敗',
        'Input_Required_Message': 'ユーザー名とパスワードを入力してください。',
        'Input_Required_Title': '入力が必要です',
        # Login Member Tutorial
        'Skip_Button': 'スキップ',
        'Next_Button': '次へ',
        # Item View, Card, Cash, eWallet Payment Option
        'Welcome_User': 'ようこそ',
        'Role_Output': 'メンバー',
        'Help_Button': 'ヘルプ',
        'Shopping_List_Button': 'ショッピングリスト',
        'Search_Products_Button': '商品検索',
        'Product_Label': '製品',
        'Detail_Label': '詳細',
        'Price_Label': '価格',
        'Barcode_Label': 'バーコード',
        'Summary_Label': '概要',
        'Remove_Label': 'アイテムを削除する',
        'Total_Products_Label': '製品数',
        'Total_Items_Label': 'アイテム数',
        'Total_Price_Label': '合計金額',
        'Total_Products_Output': '0 製品',
        'Total_Items_Output': '0 アイテム',
        'Total_Price_Output': '¥ 0.00',
        'Discount_Label':'割引', 
        'Discount_Output':'¥ 0.00',
        'Discount_Name':'10% OFF',
        'Checkout_Button': 'チェックアウトに進む',
        'Payment_Button': '支払いに進む',
        'Scan_Barcode_Push_Button': 'バーコードを開く',
        # Item View Error Message
        'Close_Barcode_Scanner': 'バーコードスキャナを閉じる',
        'Scan_Barcode_Title': 'バーコードをスキャン',
        'Scan_Barcode_Message': 'カメラの前にバーコードを配置してください。ボタンをもう一度クリックしてスキャナーを閉じます。',
        'Open_Barcode_Scanner': 'バーコードスキャナを開く',
        'Scanning_Done_Title': 'スキャン完了',
        'Scanning_Done_Message': 'バーコードのスキャンが完了しました。',
        'Scanner_Closed_Title': 'スキャナーが閉じられました',
        'Scanner_Closed_Message': '1分間スキャンがありません。バーコードスキャナーが閉じられました。',
        'Add_Remove_Title':'買い物が一時停止されました!',
        'Add_Before_Scan_Message': '追加したアイテムを削除して買い物を続けてください！',
        'Remove_Before_Scan_Message': 'アイテムを削除するにはスキャンしてください。買物を続けるためにカートに戻してください。',
        'Put_Item_Message': 'スキャンされた商品をカートの中に入れてください。',
        'Put_Item_Error_Message': '10秒後にアイテムが入れられなかったので、もう一度スキャンしてください。',
        # Payment Option
        'Welcome_User': 'いらっしゃいませ',
        'Role_Output': 'メンバー',
        'Help_Button': 'ヘルプ',
        'Payment_Label': '支払い方法を選択',
        'Card_Label': '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">クレジットカード支払い</span></p></body></html>',
        'E_Wallet_Label': '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">電子マネー支払い</span></p></body></html>',
        'Cash_Label': '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">現金支払い</span></p></body></html>',
        'Card_Payment': 'クレジットカード支払い',
        'E_Wallet_Payment': '電子マネー支払い',
        'Cash_Payment': '現金支払い',
        'Voucher_Label': '利用可能なバウチャー',
        # Feedback 
        'Finish_Push_Button': 'ショッピングを完了する',
        'Feedback_Push_Button': 'フィードバックを提供する',
        'Thankyou_Label': '親愛なるショッパー、ありがとうございます！',
        'Feedback_Paragraph': '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style="font-family:'Montserrat'; font-size:20px; font-weight:400; font-style:normal;">
<p align="center" style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-family:'MS Shell Dlg 2'; font-size:16pt;">貴重なご意見をいただきありがとうございます！</span></p>
<p align="center" style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-family:'MS Shell Dlg 2'; font-size:16pt;">最近の </span><span style="font-family:'MS Shell Dlg 2'; font-size:16pt; font-weight:600;">IM.AI Cart</span><span style="font-family:'MS Shell Dlg 2'; font-size:16pt;"> の利用体験についてのご意見をお聞かせいただき、弊社のサービス向上にご協力いただけることを嬉しく思います。 </span></p>
<p align="center" style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-family:'MS Shell Dlg 2'; font-size:16pt;">お客様のフィードバックは、私たちにとって非常に貴重です。 </span></p></body></html>''',
        # Search
        'Search_Line_Edit': '商品を検索...',
        # Feedback 
        'Finish_Button': 'ショッピングを終える',
        'Question_1': '当社のスマートショッピングカートを使用した総合的な体験について、どのように評価しますか？',
        'Q1_Answer_1': '素晴らしい',
        'Q1_Answer_2': '非常に悪い',
        'Q1_Answer_3': '良い',
        'Q1_Answer_4': '悪い',
        'Q1_Answer_5': '中立',
        'Question_2': 'スマートショッピングカートのインターフェースをどの程度使いやすいと感じましたか？',
        'Q2_Answer_1': '非常に使いやすい',
        'Q2_Answer_2': '全く使いやすくない',
        'Q2_Answer_3': 'とても使いやすい',
        'Q2_Answer_4': '少し使いやすい',
        'Q2_Answer_5': 'まあまあ使いやすい',
        'Question_3': 'スマートカートによる製品認識の精度について、どれくらい満足しましたか？',
        'Q3_Answer_1': 'いいえ',
        'Q3_Answer_2': 'はい',
        'Question_4': 'スマートカートは、お買い物の効率を向上させましたか？',
        'Q4_Answer_1': '非常に満足',
        'Q4_Answer_2': '不満',
        'Q4_Answer_3': '非常に不満',
        'Q4_Answer_4': '満足',
        'Q4_Answer_5': '中立',
        'Question_5': 'スマートショッピングカートを友人や家族にお勧めしますか？',
        'Q5_Answer_1': '非常にお勧めします',
        'Q5_Answer_2': '中立',
        'Q5_Answer_3': '少しお勧めします',
        'Q5_Answer_4': '全くお勧めしません',
        'Q5_Answer_5': 'とてもお勧めします',
    },
    # Add more languages as needed
}