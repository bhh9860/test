from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

import base64

def get_menu_url(date):
    return f"https://www.mokpo.ac.kr/www/275/subview.do?md=d&udtDt={date.replace('-', '')}"

def get_lunch_menu(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)

        # 중식 메뉴 요소 찾기
        diet_list_wrap = driver.find_element("css selector", "ul._dietListWrap")
        menu_items = diet_list_wrap.find_elements("css selector", "li > dl")
        dataResult = []

        for item in menu_items:
            dt_text = item.find_element("css selector", "dt").text
            dd_texts = [dd.text for dd in item.find_elements("css selector", "dd")]
            menu_text = f"{dt_text}: {', '.join(dd_texts)}"
            dataResult.append(menu_text)

        # 현재 요일 구하기
        today_weekday = datetime.now().weekday()

        # 현재 요일에 해당하는 데이터 출력
        result = "중식 메뉴: "
        result += dataResult[today_weekday]
        realResult = result.encode("utf-8")
        result = base64.b64encode(realResult)
        print(result)
        # print(f"중식 메뉴: \n{dataResult[today_weekday]}")
    except Exception as e:
        result = "Error: "
        result += e
        result += "\n중식 메뉴를 찾을 수 없습니다."
        # print(f"Error: {e}")
        # print("중식 메뉴를 찾을 수 없습니다.")
        print(result)
    finally:
        driver.quit()

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    menu_url = get_menu_url(today)
    get_lunch_menu(menu_url)

if __name__ == '__main__':
    main()