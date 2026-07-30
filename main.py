import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart School Management (SMKS19)")

# Colors
WHITE = (255, 255, 255)
BLUE = (22, 88, 123)
LIGHTBLUE = (132, 179, 206)
BUTTER = (225, 237, 168)

SHADOW = (180, 180, 180)

# Font
font = pygame.font.SysFont("Arial", 50)

question_font = pygame.font.SysFont("Arial", 36)

small_font = pygame.font.SysFont("Arial", 28)

# Start button
button = pygame.Rect(375, 250, 250, 80)

# Pillars
pillar1 = pygame.Rect(60, 150, 250, 400)
pillar2 = pygame.Rect(375, 150, 250, 400)
pillar3 = pygame.Rect(690, 150, 250, 400)

answer1 = pygame.Rect(150,350,300,80)
answer2 = pygame.Rect(550,350,300,80)
back_button = pygame.Rect(50,50,150,60)

# Close button
close_button = pygame.Rect(900, 30, 50, 50)


quiz_questions = {

    "Disiplin": [

        {
            "question": "Apakah maksud disiplin?",
            "choices": [
                "Mematuhi peraturan",
                "Menghormati ibu bapa"
            ],
            "answer": "Mematuhi peraturan"
        },

        {
            "question": "Apakah tindakan yang betul semasa melihat seseorang dibuli?",
            "choices": [
                "Ikuti pembuli membuli",
                "Laporkan kepada guru"
            ],
            "answer": "Laporkan kepada guru"
        },

        {
            "question": "Pelajar yang berdisiplin akan...",
            "choices": [
                "Menyiapkan tugasan",
                "Mengabaikan kerja"
            ],
            "answer": "Menyiapkan tugasan"
        }

    ],


    "Kebersihan": [

        {
            "question": "Dimanakah patut membuang sampah?",
            "choices": [
                "Tong sampah",
                "Lantai kelas"
            ],
            "answer": "Tong sampah"
        },

        {
            "question": "Mengapakah kita perlu menjaga kebersihan?",
            "choices": [
                "Agar kelas lebih selesa",
                "Untuk membuat kelas kotor"
            ],
            "answer": "Agar kelas lebih selesa"
        }

    ],


    "Keselamatan": [

        {
            "question": "Apakah tindakan yang perlu dilakukan ketika berlaku kecemasan?",
            "choices": [
                "Ikut arahan guru",
                "Berlari tanpa arah"
            ],
            "answer": "Ikut arahan guru"
        },

        {
            "question": "Apakah nombor kecemasan di Malaysia?",
            "choices": [
                "999",
                "123"
            ],
            "answer": "999"
        }

    ]

}

# Current screen
game_state = "start"


current_question = 0
result = ""
answered = False

answer_time = 0

score = 0
final_score = 0

quiz_finished = False
finish_time = 0

running = True

while running:

    mouse = pygame.mouse.get_pos()

    # -------- EVENTS --------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Close game button
            if close_button.collidepoint(mouse):

                running = False

            if game_state == "quiz":

                if back_button.collidepoint(mouse):

                    game_state = "menu"
                    result = ""

            if game_state == "quiz":

                question = quiz_questions[current_pillar][current_question]


                if answer1.collidepoint(mouse) and answered == False:

                    if question["choices"][0] == question["answer"]:

                        result = "Betul!"
                        score += 1

                    else:
                        result = "Salah! Jawapan: " + question["answer"]

                    answered = True
                    answer_time = time.time()


                elif answer2.collidepoint(mouse) and answered == False:

                    if question["choices"][1] == question["answer"]:

                        result = "Betul!"
                        score += 1

                    else:
                        result = "Salah! Jawapan: " + question["answer"]

                    answered = True
                    answer_time = time.time()


            if game_state == "start":

                if button.collidepoint(mouse):
                    game_state = "menu"

            elif game_state == "menu":


                if pillar1.collidepoint(mouse):

                    current_pillar = "Disiplin"
                    current_question = 0
                    result = ""
                    answered = False
                    answer_time = 0
                    score = 0
                    quiz_finished = False
                    game_state = "quiz"


                elif pillar2.collidepoint(mouse):

                    current_pillar = "Kebersihan"
                    current_question = 0
                    result = ""
                    answered = False
                    answer_time = 0
                    score = 0
                    quiz_finished = False
                    game_state = "quiz"


                elif pillar3.collidepoint(mouse):

                    current_pillar = "Keselamatan"
                    current_question = 0
                    result = ""
                    answered = False
                    answer_time = 0
                    score = 0
                    quiz_finished = False
                    game_state = "quiz"


    # -------- DRAW START SCREEN --------
    if game_state == "start":

        screen.fill(WHITE)

        if button.collidepoint(mouse):
            pygame.draw.rect(screen, LIGHTBLUE, button, border_radius=20)
        else:
            pygame.draw.rect(screen, BLUE, button, border_radius=20)

        title = font.render("Smart School Management", True, BLUE)
        screen.blit(title, (260, 120))

        text = font.render("MULA", True, BUTTER)
        screen.blit(text, (445, 260))

    # -------- DRAW MENU --------
    elif game_state == "menu":

        screen.fill((240, 235, 220))

        title = font.render("Pilih soalan yang anda mahukan", True, BLUE)
        screen.blit(title, (250, 50))

        if pillar1.collidepoint(mouse):
            pygame.draw.rect(screen, LIGHTBLUE, pillar1, border_radius=25)
        else:
            shadow1 = pillar1.move(5,5)

            pygame.draw.rect(
                screen,
                SHADOW,
                shadow1,
                border_radius=25
            )

            pygame.draw.rect(
                screen,
                BLUE,
                pillar1,
                border_radius=25
            )

        if pillar2.collidepoint(mouse):
            pygame.draw.rect(screen, LIGHTBLUE, pillar2, border_radius=25)
        else:
            shadow2 = pillar2.move(5,5)

            pygame.draw.rect(
                screen,
                SHADOW,
                shadow2,
                border_radius=25
            )

            pygame.draw.rect(
                screen,
                BLUE,
                pillar2,
                border_radius=25
            )

        if pillar3.collidepoint(mouse):

            pygame.draw.rect(screen, LIGHTBLUE, pillar3, border_radius=25)

        else:
            shadow3 = pillar3.move(5,5)

            pygame.draw.rect(
                screen,
                SHADOW,
                shadow3,
                border_radius=25
            )

            pygame.draw.rect(
                screen,
                BLUE,
                pillar3,
                border_radius=25
            )
        text1 = font.render("Disiplin", True, BUTTER)
        text2 = font.render("Kebersihan", True, BUTTER)
        text3 = font.render("Keselamatan", True, BUTTER)

        screen.blit(text1, (117, 320))
        screen.blit(text2, (405, 320))
        screen.blit(text3, (700, 320))

        # Draw close button

        if close_button.collidepoint(mouse):

            pygame.draw.rect(
                screen,
                LIGHTBLUE,
                close_button,
                border_radius=15
            )

        else:

            pygame.draw.rect(
                screen,
                BLUE,
                close_button,
                border_radius=15
            )




        close_font = pygame.font.SysFont("Arial",40)

        close_text = close_font.render(
            "X",
            True,
            BUTTER
        )

        screen.blit(
            close_text,
            close_text.get_rect(center=close_button.center)
        )

        # -------- DRAW QUIZ --------
    elif game_state == "quiz":

        if answered:

            if time.time() - answer_time > 2:

                if current_question < len(quiz_questions[current_pillar]) - 1:

                    current_question += 1
                    result = ""
                    answered = False

                else:

                    final_score = score

                    quiz_finished = True

                    finish_time = time.time()

                    answered = False

        if quiz_finished:

            screen.fill((240,235,220))


            title = font.render(
                "Tahniah!",
                True,
                BLUE
            )

            screen.blit(
                title,
                title.get_rect(center=(WIDTH//2,150))
            )


            message = small_font.render(
                "Anda telah menyelesaikan quiz ini",
                True,
                BLUE
            )

            screen.blit(
                message,
                message.get_rect(center=(WIDTH//2,230))
            )


            score_text = font.render(
                str(final_score) + " / " + str(len(quiz_questions[current_pillar])),
                True,
                BLUE
            )

            screen.blit(
                score_text,
                score_text.get_rect(center=(WIDTH//2,330))
            )


            back_menu = small_font.render(
                "Kembali ke menu...",
                True,
                BLUE
            )

            screen.blit(
                back_menu,
                back_menu.get_rect(center=(WIDTH//2,430))
            )




            if time.time() - finish_time > 4:

                game_state = "menu"

                quiz_finished = False

                score = 0

                current_question = 0

        if not quiz_finished:

            screen.fill((240,235,220))

            question = quiz_questions[current_pillar][current_question]

            # Question title
            question_text = question_font.render(
                "Soalan " + str(current_question + 1) + "/"
                + str(len(quiz_questions[current_pillar]))
                + ": "
                + question["question"],
                True,
                BLUE
            )

            question_rect = question_text.get_rect(center=(WIDTH//2, 170))

            screen.blit(question_text, question_rect)

            # Answer buttons
            pygame.draw.rect(
                screen,
                SHADOW,
                answer1.move(4,4),
                border_radius=20
            )

            pygame.draw.rect(
                screen,
                BLUE,
                answer1,
                border_radius=20
            )

            pygame.draw.rect(
                screen,
                SHADOW,
                answer2.move(4,4),
                border_radius=20
            )

            pygame.draw.rect(
                screen,
                BLUE,
                answer2,
                border_radius=20
            )


            # Answer text
            choice1 = small_font.render(
                question["choices"][0],
                True,
                BUTTER
            )

            choice2 = small_font.render(
                question["choices"][1],
                True,
                BUTTER
            )

            screen.blit(choice1, (170,380))
            screen.blit(choice2, (570,380))

            # Result
            result_text = small_font.render(
                result,
                True,
                BLUE
            )

            screen.blit(result_text, (220,500))

            score_text = small_font.render(
                "Skor: " + str(score),
                True,
                BLUE
            )

            screen.blit(score_text,(750,100))

            # Back button
            pygame.draw.rect(screen, BLUE, back_button, border_radius=20)

            back_text = small_font.render(
                "BACK",
                True,
                BUTTER
            )

            screen.blit(back_text, (85,65))



    pygame.display.update()

pygame.quit()
sys.exit()