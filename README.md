Machine Learning Stock and Crypto AI App

Detaylı Proje Açıklaması: Yapay Zekâ Destekli Hisse Senedi ve Kripto Para Tahmin Mobil Uygulaması (StockSageAI)
Proje Hakkında Genel Bilgi
StockSageAI, mobil platformlarda hisse senedi ve kripto para fiyatlarını tahmin etmek için yapay zekâ ve makine öğrenimi teknolojilerini kullanan bir mobil uygulamadır. Bu uygulama, yatırımcıların ve traderların yatırım kararlarını daha bilinçli ve güvenilir bir şekilde almasını sağlamak amacıyla geliştirilmiştir. Kullanıcılar, uygulama sayesinde geçmiş fiyat verilerini analiz ederek gelecekteki fiyat hareketlerini öngörebilir ve potansiyel yatırım fırsatlarını değerlendirebilir.

Proje Amacı
Projenin temel amacı, kullanıcıların finansal piyasalar hakkında daha fazla bilgi sahibi olmalarını ve bu bilgileri kullanarak daha iyi yatırım kararları vermelerini sağlamaktır. Bu amaç doğrultusunda uygulama, hem hisse senedi hem de kripto para piyasalarına yönelik analizler ve tahminler sunar. Bu tahminler, çeşitli makine öğrenimi algoritmaları ve teknik analiz araçları kullanılarak elde edilir.

Kullanılan Teknolojiler ve Araçlar
Proje, Python programlama dili ve çeşitli kütüphaneler kullanılarak geliştirilmiştir. Kullanılan başlıca kütüphaneler şunlardır:

Pandas: Veri analizi ve işleme.
NumPy: Bilimsel hesaplamalar ve matematiksel işlemler.
Matplotlib ve Seaborn: Veri görselleştirme.
Scikit-Learn: Makine öğrenimi algoritmaları.
TensorFlow ve Keras: Derin öğrenme modelleri (LSTM ve GRU).
TA-Lib: Teknik analiz göstergeleri ve sinyalleri.
YFinance: Yahoo Finance API'sini kullanarak piyasa verisi indirme.
FastAPI: API geliştirme ve entegrasyon.
Veri Toplama ve İşleme Süreci
Proje, veri toplama ve işleme süreçlerini titizlikle takip eder:

Veri Toplama: Geçmiş fiyat verileri, Yahoo Finance ve CryptoCompare API'leri kullanılarak toplanır. Hisse senetleri ve kripto paralar için ayrı ayrı veri kümeleri oluşturulur.
Veri Temizleme ve Ön İşleme: Toplanan veriler, eksik verilerin doldurulması, aykırı değerlerin tespiti ve düzeltilmesi, ve veri normalizasyonu gibi işlemlerden geçirilir.
Özellik Mühendisliği: Hareketli ortalamalar, fiyat değişim oranları ve teknik göstergeler (RSI, MACD, Bollinger Bands gibi) hesaplanarak modele entegre edilir.
Makine Öğrenimi Modelleri
Proje kapsamında kullanılan başlıca makine öğrenimi modelleri şunlardır:

LSTM (Long Short-Term Memory): Zaman serisi verileri üzerinde fiyat tahmini yapmak için kullanılır. LSTM, uzun dönemli bağımlılıkları modelleyebilir ve bu sayede finansal zaman serilerinde sıklıkla görülen değişkenlikleri tahmin edebilir.
GRU (Gated Recurrent Unit): LSTM modeline benzer bir yapay sinir ağıdır, ancak daha az hesaplama gücü gerektirir ve bazı durumlarda daha hızlı öğrenme sağlar.
Rastgele Ormanlar (Random Forests) ve Karar Ağaçları (Decision Trees): Basit modeller olup, temel sınıflandırma ve regresyon problemleri için kullanılır.
Lineer Regresyon ve SVM (Support Vector Machines): Hisse senedi ve kripto para fiyatlarının doğrusal ve doğrusal olmayan desenlerini yakalamak için kullanılır.
Teknik Analiz ve Sinyal Üretimi
Uygulama, teknik analiz göstergeleri ve sinyallerini kullanarak alım-satım sinyalleri üretir. Kullanılan bazı teknik analiz araçları şunlardır:

Bollinger Bantları: Fiyatın belirli bir aralık içinde dalgalanmasını ölçer.
RSI (Relative Strength Index): Piyasanın aşırı alım veya satım durumunda olup olmadığını gösterir.
MACD (Moving Average Convergence Divergence): Fiyat trendlerinin yönünü ve momentumunu belirler.
Ichimoku Bulutu: Fiyat trendleri, destek ve direnç seviyeleri hakkında bilgi sağlar.
Parabolik SAR (Stop and Reverse): Potansiyel dönüş noktalarını belirler.
Mobil Uygulama Geliştirme ve Kullanıcı Arayüzü
Uygulamanın mobil kısmı, kullanıcıların kolaylıkla kullanabileceği ve bilgileri hızlı bir şekilde erişebileceği bir arayüz sunar. Başlıca özellikler şunlardır:

Gerçek Zamanlı Veri Entegrasyonu: Kullanıcılar anlık fiyat bilgilerini ve tahminleri gerçek zamanlı olarak görebilir.
Etkin ve Kullanıcı Dostu Arayüz: Basit ve temiz bir tasarımla kullanıcı deneyimini artırır.
Anlık Bildirimler ve Uyarılar: Belirli fiyat seviyelerine ulaşıldığında veya tahmin edilen belirli koşullar sağlandığında kullanıcılara uyarılar gönderilir.
Sonuçlar ve Performans Değerlendirmesi
Proje, kullanılan modellerin performansını Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE) ve R2 gibi metriklerle değerlendirir. Sonuçlar, özellikle LSTM ve GRU modellerinin zaman serisi tahmininde üstün performans gösterdiğini ortaya koymuştur. En iyi sonuçlar, Backward Fill yöntemi kullanılarak elde edilmiştir:

LSTM Modeli: MAE: 254.82, MSE: 123719.61, RMSE: 351.73, R2: 0.9819
GRU Modeli: MAE: 223.85, MSE: 96198.16, RMSE: 310.15, R2: 0.9859
Sonuç
StockSageAI, yatırımcılara ve traderlara yapay zekâ destekli bir platform sunarak, piyasa hareketlerini analiz etmeleri ve daha bilinçli yatırım kararları vermeleri için bir araç sağlar. Bu proje, finansal piyasaların dinamik yapısını anlamak ve tahmin edebilmek için gelişmiş algoritmalar ve analiz tekniklerini bir araya getirir. Kullanıcılar, bu uygulama sayesinde piyasalar hakkında derinlemesine bilgi sahibi olabilir ve finansal hedeflerine ulaşmak için stratejilerini optimize edebilirler.

Machine Learning Stock and Crypto AI App is a comprehensive application designed to predict stock and cryptocurrency prices using advanced machine learning algorithms. The project aims to provide investors and traders with accurate predictions to make informed decisions. The application fetches real-time data from various APIs, processes the data, and applies machine learning models to predict future price trends.

Features
Real-Time Data Fetching: Fetches the latest stock and cryptocurrency data from reliable APIs.
Data Analysis: Performs in-depth analysis of the fetched data, including technical indicators and historical trends.
Machine Learning Models: Implements various machine learning algorithms to predict future prices.
Visualization: Provides detailed visualizations of the data and prediction results.
User-Friendly Interface: Easy-to-navigate interface for both novice and experienced traders.
Tech Stack
Programming Languages: Python
Libraries: Pandas, NumPy, Scikit-Learn, TensorFlow, Keras, Matplotlib, Seaborn
APIs: Alpha Vantage, Binance API, Yahoo Finance API
Tools: Jupyter Notebook, Visual Studio Code
Installation
To run this project locally, follow these steps:

Clone the repository:

git clone https://github.com/kavalugur/Machine-Learning-Stock-Crypto-AI-App.git
cd Machine-Learning-Stock-Crypto-AI-App



Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Install required packages:

pip install -r requirements.txt


Set up API keys: Rename config_example.py to config.py and add your API keys:

API_KEY_ALPHA_VANTAGE = 'your_alpha_vantage_api_key'
API_KEY_BINANCE = 'your_binance_api_key'


Usage
To start the application, run the following command:
python main.py
This command will initialize the application, fetch the data, perform predictions, and display the results.



API Integration
This project uses several APIs to fetch real-time data:

Alpha Vantage API: Provides stock market data.
Binance API: Fetches cryptocurrency market data.
Yahoo Finance API: Supplies additional financial data and metrics.
Ensure to register and obtain your API keys from these platforms and update the config.py file accordingly.

Data Sources
The application utilizes both historical and real-time data from:

Stock exchanges like NYSE and NASDAQ.
Cryptocurrency exchanges like Binance and Coinbase.
Machine Learning Models
The following machine learning models have been implemented:

Linear Regression: For simple, linear relationships.
Random Forest: For capturing complex patterns and reducing overfitting.
Long Short-Term Memory (LSTM): A recurrent neural network suited for time series prediction.
XGBoost: An optimized gradient boosting framework for robust predictions.
Each model is evaluated based on accuracy, mean squared error, and other performance metrics.

Results
The model performance and prediction results are documented in the notebooks/ directory. Key highlights include:

Model Accuracy: Achieved over 80% accuracy in predicting daily closing prices.
Visualization: Graphs and plots showcasing the trends and model predictions.
