import flet as ft

def main(page: ft.Page):
    # 모바일 레이아웃 및 테마 설정
    page.title = "파이썬 모바일 앱 예제"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 상태 변수
    number = ft.Text(value="0", size=40, weight=ft.FontWeight.BOLD)

    def button_click(e):
        # 클릭 이벤트 처리
        current_val = int(number.value)
        number.value = str(current_val + 1)
        page.update()

    def button_1_click(e):
        # 클릭 이벤트 처리
        current_val = int(number.value)
        number.value = str(current_val - 1)
        page.update()



    # UI 구성 요소 추가
    page.add(
        ft.Text("간단한 카운터 앱", size=20, weight=ft.FontWeight.W_500),
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        number,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        ft.Button("숫자 증가 (+1)", on_click=button_click),
        ft.Button("숫자 감소 (-1)", on_click=button_1_click),
    )



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    ft.run(main, port=port, host="0.0.0.0")