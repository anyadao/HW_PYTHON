# 27.	* По рзелульаттам илссеовадний одонго анлигйсокго унвиертисета, не иеемт занчнеия, в кокам пряокде
# рсапожолены бкувы в солве. Галвоне, чотбы преавя и пслоендяя бквуы блыи на мсете. Осатьлыне бкувы мгоут селдовтаь
# в плоонм бсепордяке, все-рвано ткест чтаитсея без побрелм. Пичрионй эгото ялвятеся то, что мы чиатем не кдаужю бкуву
#  по отдльенотси, а все солво цликеом.Напишите функцию, которая преобразует переданный ей текст способом,
# похожим на описанный выше. В качестве алгоритма перемешивания букв в слове используйте следующий:
#Для каждого слова в тексте:
# 	1. Фиксируем первый и последний символы слова.
# 	2. Из оставшихся берём первые три символа, произвольно перемешиваем.
# 	3. Полученную тройку фиксируем, т.е. она уже не будет участвовать в дальнейшем перемешивании.
# 	4. Повторяем пункт 2, пока незафиксированные символы не кончатся.
# def pemrtuate(text): # returns permuted text
# 	pass
# Ccылка по теме: https://geektimes.ru/post/148896/


import random
import re

def pemrtuate(text):
    changed_text = ''
    space = ' '
    for word in text.split(space):
        length_for_random = len(word)
        word_length = len(word)
        fixed_length = 2
        three_symb = 3
        randomize_letters = 4
        start = 1
        fixed = []
        if word_length <= randomize_letters:
            changed_text = changed_text + word + space
        elif re.match('[.,:!?-]', word):
            changed_text = changed_text + word + space
        else:
            fixed.insert(0, word[0])
            length_for_random -= fixed_length
            while length_for_random >= three_symb:
                to_random = list(word[start:randomize_letters])
                random.shuffle(to_random)
                fixed[start:len(to_random)] = to_random[0:len(to_random)]
                length_for_random -= three_symb
                if length_for_random < three_symb:
                    fixed[randomize_letters:word_length] = word[randomize_letters: word_length-1]
                start += three_symb
                randomize_letters += three_symb
            fixed.insert(word_length - 1, word[word_length - 1])
            joined_fixed_symbols = ''.join(fixed)
            changed_text = changed_text + joined_fixed_symbols + space
    return changed_text

text = """Начало рабочего дня всегда вызывало у Уинстона глубокий непроизвольный вздох, хотя монитор и находился рядом. 
Он придвинул к себе диктограф, сдул пыль с микрофона и надел очки. Затем развернул и скрепил скрепками четыре маленьких 
бумажных цилиндрика, которые уже выскочили из пневматической почты с правой стороны рабочего стола.
В стенах его кабинки было три отверстия. Справа от диктографа располагалась маленькая пневматическая трубка для записок,
слева — трубка побольше для газет, а в боковой стенке — большая продолговатая щель, защищенная проволочной сеткой."""
print(pemrtuate(text))

