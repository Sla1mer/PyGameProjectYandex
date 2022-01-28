import pygame
import sys
from Settings import get_volume
from draw_text import draw_text
from load_img import load_image

pygame.init()
sc = pygame.display.set_mode((1820, 900))

pygame.mixer.music.load('sound/start_music.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(get_volume())
first_scene_1 = '''Я проснулся от ужасающего звука с улицы, во мне закралась небольшая тревога. '''
first_scene_2 = '''Выглянул в окно, я вижу страшное: на улице всё горит, какие-то железные махины уничтожают город.'''
first_scene_3 = '''От увиденного я начал падать в обморок.....'''
second_scene_1 = '''Прошло часа два,я очнулся, лежа на полу и не зная что делать'''
second_scene_2 = '''Я ущемнул себя, проверив не сплю ли я. Да я Семён Персунов, мне 22 года, я учусь в  ИНиГ СФУ.'''
second_scene_3 = '''Да. Я точно не сплю, и все происходит наяву.'''
second_scene_4 = '''Очень хотелось есть, но в холодильнике пусто. Пойду на вылазку, все равно умру с голода....'''
third_scene_1 = '''Вот я на улице, страшно. Вокруг всё горело, падали здания'''
third_scene_2 = '''Передо мной какой-то железный гигант, я тут же сворачиваю за угол'''
third_scene_3 = '''Бац. Я на пустыре, как? Тут же вчера был торговый центр'''
third_scene_4 = '''Похоже,я вдохнул какой-то токсин. Я падаю в обморок. Опять.'''
third_scene_5 = '''Последнее что я вижу - силует незнакомца.'''
fourth_scene_1 = '''Не знаю сколько я спал... Я очнулся в каком-то подвале. Рядом сидел молодой человек'''
fourth_scene_2 = '''Незнакомец: Ооо ты встал наконец-то. А то я думал потерял последнего.. А ведь еле ускользнули.'''
fourth_scene_3 = '''*я про себя* Кто? Что? Почему я последний?'''
fourth_scene_4 = '''Незнакомец продолжал: началось вторжение от неизвестных объектов, наш город разрушен на 80%'''
fourth_scene_5 = '''Ты и я наверное единственные кто уцелели. Подвал в котором мы находимся я берег на случай ядерной войны'''
fourth_scene_6 = '''Александр меня звать - добавил незнакомец'''
fourth_scene_7 = '''Семен - ответил я в ответ. Александр: Ну ладно Сёмен, будем знако...'''
fourth_scene_8 = '''Резко комната наполняется белым светом... Ииии щёлчок!'''
in_sovenok_1 = '''Каким то образом я с Алексом оказался в тунеле. Вокруг темно. '''
in_sovenok_2 = '''Идем на ощупь, я и Саша молчит, вдруг видим -  лучик света'''
in_sovenok_3 = ''' Ого, это люк - Сказал мой спутник.'''
in_sovenok_4 = '''Мы полезли на верх - оказались на какой-то площади'''
in_sovenok_5 = '''*Я говорю Алексу* Ничего не понимаю, что за чертовщи.... *Еще одна вспышка*'''
in_sovenok_6 = '''...'''
drago_1 = '''Мы появились около дракона. Испугавшись, я отошёл на шаг. Стоп. Я что маг?'''
drago_2 = '''Моё тело координально изменилось. Теперь на мне обмотки... В руках копье...'''
drago_3 = '''*Про себя, смотря на Александра* Ооо Александр тоже изменил внешний вид....'''
drago_4 = '''Перебив мои мысли, заговорила дракониха, не дракон.'''
drago_5 = '''Драконихa: Вы стали избранными. Вы должны спасти свою цивилизацию '''
drago_5_1 = '''Заставив время идти вспять, и изменив прошлое....'''
drago_6 = '''Я дракониха времени вселенной, пыталась переместить из вашей вселенной в мою'''
drago_6_1 = '''Кхм, простите, что не с первого раза получилось'''
drago_7 = '''Вы должны отправиться к дьяволу, он вам расскажет как всё исправить.'''
drago_8 = '''Александр спрашивает: А почему вы не можете это сделать?'''
drago_9 = '''Дракониха отвечает: я бессмертна, а дьявол имеет дело только со смертными. '''
drago_10 = '''Выслушав ответ, мы отправились в логово к бесу'''
way_1 = '''Мы начали долгий путь, по карте которую дала нам дракониха'''
way_2 = '''Мы пошли через лес, так нам показалось короче'''
way_3 = '''*Спустя три дня*'''
way_4 = '''Уже три дня как мы идем лесной чащей, мы не хотим ни еды ни воды.'''
way_4_1 = '''Странное ощущение, возможно особенности этого мира  '''
way_5 = '''Спустя неделю'''
way_6 = '''Ура лес закончился, перед нами странное каменное плато, карта указывает идти через него. '''
way_7 = '''Александр задумался и спросил: Думаешь хорошая идея идти туда?'''
way_7_1 = '''Может нафиг вообще спасать мир? Нам и так хорошо'''
way_8 = '''Вот подумай, мы не нуждаемся в ресурсах, живи как хочешь!'''
way_9 = '''Наперекор словам Алекса я пошел. Он за мной.'''
way_9_1 = '''Еще спустя неделю'''
way_10 = '''Перед нами открылся лавовый замок дьявола. Всего спустя неделю пути то!'''
way_11 = '''Тут перед нами, откуда не возмись, появился бес. Веселый черт говорит: я ЗнАю ЧТо вАМ нАдО!'''
way_12 = '''Перебив нас, он продолжил: Я расскажу вам секрет, но только условие!'''
way_13 = '''Мы ответили: какое?'''
way_14 = '''Дьявол: вам надо сыграть в игру кардмастер, против друг друга.'''
way_14_1 = '''НА ВЫЖИВАНИЕ. КТО ПОБЕДИТ ТОТ ПОЛУЧАЕТ ИНФОРМАЦИЮ ПО СПАСЕНИЮ МИРА'''
way_15 = '''АХХАХАХАХАХАХАХААХХААХАХАХАХ - продолжал зларадствовать он'''
way_16 = '''Нам пришлось согласиться с его требованиями.....'''
way_17 = '''*А что было дальше, вы узнаете во второй часте нашей игры - Кардмастер: наследие.'''
way_18 = '''А пока предлагаю насладиться нашей непревосходной карточной игрой!*'''


def story(screen, screen_size):
    order_of_events = {first_scene_1: 'story/hero_room.jpg',
                       first_scene_2: 'story/hero_room.jpg',
                       first_scene_3: 'story/obmorok.jpg',
                       second_scene_1: 'story/obmorok.jpg',
                       second_scene_2: 'story/obmorok.jpg',
                       second_scene_3: 'story/obmorok.jpg',
                       second_scene_4: 'story/hero_room.jpg',
                       third_scene_1: 'story/shoke.jpg',
                       third_scene_2: 'story/shoke.jpg',
                       third_scene_3: 'story/shoke.jpg',
                       third_scene_4: 'story/obmorok.jpg',
                       third_scene_5: 'story/sanya_first.png',
                       fourth_scene_1: 'story/catacombs.jpg',
                       fourth_scene_2: 'story/catacombs.jpg',
                       fourth_scene_3: 'story/catacombs.jpg',
                       fourth_scene_4: 'story/catacombs.jpg',
                       fourth_scene_5: 'story/catacombs.jpg',
                       fourth_scene_6: 'story/catacombs.jpg',
                       fourth_scene_7: 'story/catacombs.jpg',
                       fourth_scene_8: 'story/tp_to_sovenok.jpg',
                       in_sovenok_1: 'story/cato1.jpg',
                       in_sovenok_2: 'story/cato2.jpg',
                       in_sovenok_3: 'story/to_genda.jpg',
                       in_sovenok_4: 'story/genda.jpg',
                       in_sovenok_5: 'story/genda.jpg',
                       in_sovenok_6: 'story/tp_to_sovenok.jpg',
                       drago_1: 'story/drago.jpg',
                       drago_2: 'story/drago.jpg',
                       drago_3: 'story/drago.jpg',
                       drago_4: 'story/drago.jpg',
                       drago_5: 'story/drago.jpg',
                       drago_5_1: 'story/drago.jpg',
                       drago_6: 'story/drago.jpg',
                       drago_6_1: 'story/drago.jpg',
                       drago_7: 'story/drago.jpg',
                       drago_8: 'story/drago.jpg',
                       drago_9: 'story/drago.jpg',
                       drago_10: 'story/drago.jpg',
                       way_1: 'story/forest1.jpg',
                       way_2: 'story/forest1.jpg',
                       way_3: 'story/forest1.jpg',
                       way_4: 'story/forest2.jpg',
                       way_4_1: 'story/forest2.jpg',
                       way_5: 'story/way_to_hell.jpg',
                       way_6: 'story/way_to_hell.jpg',
                       way_7: 'story/way_to_hell.jpg',
                       way_7_1: 'story/way_to_hell.jpg',
                       way_8: 'story/way_to_hell.jpg',
                       way_9: 'story/way_to_hell.jpg',
                       way_9_1: 'story/way_to_hell.jpg',
                       way_10: 'story/before_hell.jpg',
                       way_11: 'story/hell.jpg',
                       way_12: 'story/hell.jpg',
                       way_13: 'story/hell.jpg',
                       way_14: 'story/hell.jpg',
                       way_14_1: 'story/hell.jpg',
                       way_15: 'story/hell.jpg',
                       way_16: 'story/hell.jpg',
                       way_17: 'story/hell.jpg',
                       way_18: 'story/hell.jpg',
                       }

    mainClock = pygame.time.Clock()
    running = True
    k = 0
    to_read = {}
    for id, (text, bg) in enumerate(order_of_events.items()):
        print(text)
        bg = pygame.transform.scale(load_image(bg, flag=True), (screen_size[0], screen_size[1]))
        to_read[id] = (text, bg)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    k += 1
                if event.button == 3:
                    k -= 1
        if k == 59:
            running = False
        try:
            screen.blit(to_read[k][1], (0, 0))
            draw_text(to_read[k][0], screen_size[0] // 60, (255, 255, 255), screen, screen_size[0] * 0.01,
                      screen_size[1] - screen_size[1] * 0.2)
        except KeyError:
            pass

        pygame.display.flip()
    mainClock.tick(60)