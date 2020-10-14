# main.py
# pip install pyautogui

import sys

import pyautogui

import time

import webbrowser

교실 = 'https://classroom.google.com/c/NjYwMDE1MTM4MTVa'
음악 = 'https://classroom.google.com/c/NTgwNDQ0MjgzMjBa'
사회 = 'https://classroom.google.com/c/NTY5MjA0NDU4Mzla'
과학B = 'https://classroom.google.com/c/NTgwODQzMDE1NTZa'
수학B = 'https://classroom.google.com/c/Njc2NzI4ODYwNjBa'
예술체육 = 'https://classroom.google.com/c/MTMwMjAyNTIwOTYz'
도덕 = 'https://classroom.google.com/c/NjgxMjg1Nzc3Mjha'
체육A = 'https://classroom.google.com/c/NTgwNDc1NjYxNDFa'
국어A = 'https://classroom.google.com/c/NTY4ODY5MzA5OTNa'
수학A = 'https://classroom.google.com/c/NTc0ODg2NTgwMzNa'
기술 = 'https://classroom.google.com/c/NTgwNTEzODUzMDVa'
스포츠 = 'https://classroom.google.com/c/MTI3MDgzODcwNzkx'
영어A = 'https://classroom.google.com/c/NTcyNDcxNjEyMDNa'
과학A = 'https://classroom.google.com/c/NTgwOTYwMTUxNzJa'
가정 = 'https://classroom.google.com/c/NjgxNDExOTY1ODNa'
미술 = 'https://classroom.google.com/c/NTgwNTE5MjQ1NjNa'
진로와_직업 = 'https://classroom.google.com/c/MTMxNTMzODI2ODAz'
국어B = 'https://classroom.google.com/c/NTc1MDQzNDk5NjBa'
주제선택 = 'https://classroom.google.com/c/MTMwMTk1NjM4ODA2'

classes = [[교실, 음악, 사회, 과학B, 수학B, 예술체육], [교실, 체육A, 국어A, 수학A, 주제선택], [교실, 기술, 스포츠, 영어A, 과학A, 사회], [과학A, 국어A, 영어A, 수학A, 가정, 음악, 미술], [체육A, 진로와_직업, 사회, 국어B, 도덕, 영어A, 교실]]

def get_class():
    try:
        n = time.localtime().tm_wday # 요일의 인덱스를 얻어옴

        if 4 < n: # 주말이라면 프로그램 종료
            print("today you don't have class")
            sys.exit()

        else:
            return classes[n]

    except:
        print('get_day func error')
        sys.exit()

def create_new_desktop():
    try:
        pyautogui.hotkey('winleft', 'ctrl', 'd') # 윈도우 새 창열기 단축기
    
    except:
        print('create_new_desktop func error')
        sys.exit()

def to_first(time):
    try:
        i = 0
        while i < time:
            pyautogui.hotkey('winleft', 'ctrl', 'left') # time 만큼 왼쪽으로 가기
            i = i + 1

    except:
        print('to_first error')
        sys.exit()

def open_chrome(url):
    try:
        webbrowser.open(url)
        
    except:
        print('open_chrome func error')
        sys.exit()

def main():
    today_classes = get_class()
    i = 0

    for today_class in today_classes:
        if i == 0:
            open_chrome(today_class)
        else:
            create_new_desktop()
            open_chrome(today_class)
        i += 1
        time.sleep(1)

    to_first(i)

main()