from selenium.webdriver.common.by import By

# Локаторы для тестов сайта Stellar Burgers
class WebsiteLocators:

    # Локатор для кнопки "Войти в аккаунт"
    LOGIN_INTO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
        
    # Локатор для кнопки "Оформить заказ"
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Локатор для поля ввода имени в форме регистрации
    NAME_INPUT_FORM = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
        
    # Локатор для поля ввода эл. почты в форме регистрации/входа
    EMAIL_INPUT_FORM = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
        
    # Локатор для поля ввода пароля в форме регистрации/входа
    PASSWORD_INPUT_FORM = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
        
    # Локатор для кнопки "Зарегистрироваться" в форме регистрации
    REGISTRATION_BUTTON_FORM = (By.XPATH, ".//button[text()='Зарегистрироваться']")
        
    # Локатор для кнопки-текста "Войти" в форме регистрации
    LOGIN_TEXT_LINK = (By.XPATH, ".//a[text()='Войти']")
        
    # Локатор для кнопки "Войти" в форме входа
    LOGIN_BUTTON_FORM = (By.XPATH, ".//button[text()='Войти']")
        
    # Локатор для ошибки пароля в форме регистрации
    PASSWORD_ERROR_MESSAGE = (By.XPATH, ".//p[text()='Некорректный пароль']")
    
    # Локатор для кнопки "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  

    # Локатор для кнопки "Конструктор" в меню навигации сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    
    # Локатор для лого-кнопки в меню навигации сайта
    SERVICE_LOGO_BUTTON = (By.XPATH, ".//*[contains(@class, 'AppHeader_header__logo')]")
    
    # Локатор для кнопки "Личный Кабинет" в меню навигации сайта
    ACCOUNT_BUTTON_HEADER = (By.XPATH, ".//p[text()='Личный Кабинет']")
    
    # Локатор для заголовка конструктора с текстом "Соберите бургер"
    CONSTRUCTOR_HEADER = (By.XPATH, ".//*[text()='Соберите бургер']")
    
    # Локаторы для неактивных вкладок "Булки", "Соусы" и "Начинки"
    BUNS_SECTION_INACTIVE = (By.XPATH, ".//span[text()='Булки']")
    SAUCES_SECTION_INACTIVE = (By.XPATH, ".//span[text()='Соусы']")
    STUFFINGS_SECTION_INACTIVE = (By.XPATH, ".//span[text()='Начинки']")
    
    # Локаторы для активных вкладок "Булки", "Соусы" и "Начинки"
    BUNS_SECTION_ACTIVE = (By.XPATH, ".//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab_type_current')]")
    SAUCES_SECTION_ACTIVE = (By.XPATH, ".//span[text()='Соусы']/ancestor::div[contains(@class, 'tab_tab_type_current')]")
    STUFFINGS_SECTION_ACTIVE = (By.XPATH, ".//span[text()='Начинки']/ancestor::div[contains(@class, 'tab_tab_type_current')]")
    
    