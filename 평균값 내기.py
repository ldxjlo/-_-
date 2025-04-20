import tkinter as tk
from tkinter import messagebox, simpledialog

def calculate_average_and_comment(scores):
    avg = sum(scores) / len(scores)
    if avg >= 20:
        comment = "정상 범위에 해당합니다."
    elif 11 <= avg < 12:
        comment = "경계 영역입니다. 주의가 필요합니다."
    else:
        comment = "주의가 필요합니다. 전문가의 상담을 권장합니다."
    return avg, comment

def show_previous_results_popup():
    # Tkinter 메인 루프를 위한 창을 생성
    root = tk.Tk()
    root.withdraw()  # 메인 윈도우는 숨깁니다.

    is_previous = messagebox.askquestion("이전 검사", "이전에 검사한 적이 있나요?")
    if is_previous != 'yes':
        messagebox.showinfo("안내", "좋아요! 그럼 이번 검사부터 시작해볼게요.")
        return

    # 검사 횟수 입력 받기 (반복적으로 입력받을 수 있도록 수정)
    while True:
        try:
            times = int(simpledialog.askstring("검사 횟수", "총 몇 회 검사하셨나요?"))
            if times <= 0:
                messagebox.showerror("입력 오류", "검사 횟수는 1회 이상이어야 합니다.")
                continue  # 잘못된 입력이면 다시 요청
            break  # 올바른 입력이면 반복문 종료
        except:
            messagebox.showerror("입력 오류", "검사 횟수는 숫자로 입력해주세요.")
    
    categories = ["대근육 운동", "소근육 운동", "언어 이해", "언어 표현", "사회성", "자기조절"]
    result_text = "[이전 검사 결과 평균]\n"

    for cat in categories:
        while True:  # 각 카테고리마다 입력을 받을 때 반복문을 사용
            raw = simpledialog.askstring(cat, f"[{cat}] 점수를 입력해주세요 (예: 14,15,16):")
            try:
                scores = list(map(int, raw.split(",")))
                if len(scores) != times:
                    messagebox.showerror("입력 오류", f"{times}회의 점수를 입력해야 해요.")
                    continue  # 점수 개수가 맞지 않으면 다시 입력 받기
                avg, comment = calculate_average_and_comment(scores)
                result_text += f"\n{cat} 점수: {', '.join(map(str, scores))}"
                result_text += f"\n→ 평균: {avg:.2f} / 24"
                result_text += f"\n→ 해석: {comment}\n"
                break  # 올바른 입력이면 반복문 종료
            except:
                messagebox.showerror("입력 오류", f"{cat} 점수 입력이 잘못되었어요.")
                continue  # 잘못된 입력이면 다시 요청

    result_text += f"\n총 {times}회의 검사 결과를 기반으로 계산되었습니다."
    messagebox.showinfo("결과 요약", result_text)

    root.mainloop()  # 메인 루프 시작

# 실행을 테스트하려면 이 아래에서 함수 호출
show_previous_results_popup()
