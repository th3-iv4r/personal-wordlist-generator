#12.08.2021
#th3-iv4r

from colored import fg,attr
import random
import os

os.system('pip install colored')
os.system('clear')

def colorprint(text,color):
    return "%s{}%s".format(text) % (fg(color),attr(0))

def lut_code(text):
    rev_text = text[::-1]

    return text.lower() + "\n" + text.upper() + "\n" + text.title() + "\n" + rev_text.lower() + "\n" + rev_text.upper() + "\n" + rev_text.title()

def lut_code_2(text1,text2):
    return text1.lower() + text2.lower() + "\n" + text1.title() + text2.lower() + "\n" + text1.upper() + text2.upper()

def main_code():
    try:
        create_file = open("wordlist.txt","x",encoding="utf-8")
        create_file.close()

        target_first_name = input("Target's first name: ")
        target_second_name = input("Target's second name: ")
        target_surname = input("Target's surname: ")
        target_father_name = input("Target's father's name: ")
        target_mother_name = input("Target's mother's name: ")
        target_sister_name = input("Target's sister's name: ")
        target_brother_name = input("Target's brother's name: ")
        birthday = input("Target's birthday [XX.XX.XXXX]: ")
        target_birthday = birthday.replace(".","")
        target_city = input("Target's city: ")
        target_company_name = input("Target's company name: ")
        target_first_pet = input("Target's first pet: ")
        target_second_pet = input("Target's second pet: ")

        targets_gf_bf_first_name = input("Target's girlfriend/boyfriend first name: ")
        targets_gf_bf_second_name = input("Target's girlfriend/boyfriend second name: ")
        targets_gf_bf_surname = input("Target's girlfriend/boyfriend surname name: ")

        add_keyword = input("Type the keywords you want to be found [Put ',' between keywords]: ")
        add_keyword = add_keyword.split(",")

        def group2rev(text):
            text = f"""{lut_code_2(text,text)}
{lut_code_2(target_second_name,text)}
{lut_code_2(target_surname,text)}
{lut_code_2(target_father_name,text)}
{lut_code_2(target_mother_name,text)}
{lut_code_2(target_sister_name,text)}
{lut_code_2(target_brother_name,text)}
{lut_code_2(target_birthday,text)}
{lut_code_2(target_city,text)}
{lut_code_2(target_company_name,text)}
{lut_code_2(target_first_pet,text)}
{lut_code_2(target_second_pet,text)}
{lut_code_2(targets_gf_bf_first_name,text)}
{lut_code_2(targets_gf_bf_second_name,text)}
{lut_code_2(targets_gf_bf_surname,text)}"""
            return text

        def group2(text):
            text = f"""{lut_code_2(text,text)}
{lut_code_2(text,target_second_name)}
{lut_code_2(text,target_surname)}
{lut_code_2(text,target_father_name)}
{lut_code_2(text,target_mother_name)}
{lut_code_2(text,target_sister_name)}
{lut_code_2(text,target_brother_name)}
{lut_code_2(text,target_birthday)}
{lut_code_2(text,target_city)}
{lut_code_2(text,target_company_name)}
{lut_code_2(text,target_first_pet)}
{lut_code_2(text,target_second_pet)}
{lut_code_2(text,targets_gf_bf_first_name)}
{lut_code_2(text,targets_gf_bf_second_name)}
{lut_code_2(text,targets_gf_bf_surname)}"""
            return text

        file_context = f"""{lut_code(target_first_name)}
{lut_code(target_second_name)}
{lut_code(target_surname)}
{lut_code(target_father_name)}
{lut_code(target_mother_name)}
{lut_code(target_sister_name)}
{lut_code(target_brother_name)}
{target_birthday}
{target_city}
{lut_code(target_company_name)}
{lut_code(target_first_pet)}
{lut_code(target_second_pet)}
{lut_code(targets_gf_bf_first_name)}
{lut_code(targets_gf_bf_second_name)}
{lut_code(targets_gf_bf_surname)}
{group2(target_first_name)}
{group2(target_second_name)}
{group2(target_surname)}
{group2(target_father_name)}
{group2(target_mother_name)}
{group2(target_sister_name)}
{group2(target_brother_name)}
{group2(target_birthday)}
{group2(target_city)}
{group2(target_company_name)}
{group2(target_first_pet)}
{group2(target_second_pet)}
{group2(targets_gf_bf_first_name)}
{group2(targets_gf_bf_second_name)}
{group2(targets_gf_bf_surname)}
{group2rev(target_first_name)}
{group2rev(target_second_name)}
{group2rev(target_surname)}
{group2rev(target_father_name)}
{group2rev(target_mother_name)}
{group2rev(target_sister_name)}
{group2rev(target_brother_name)}
{group2rev(target_birthday)}
{group2rev(target_city)}
{group2rev(target_company_name)}
{group2rev(target_first_pet)}
{group2rev(target_second_pet)}
{group2rev(targets_gf_bf_first_name)}
{group2rev(targets_gf_bf_second_name)}
{group2rev(targets_gf_bf_surname)}
{lut_code(target_first_name + "12345")}
{lut_code(target_second_name + "12345")}
{lut_code(target_surname + "12345")}
{lut_code(target_father_name + "12345")}
{lut_code(target_mother_name + "12345")}
{lut_code(target_sister_name + "12345")}
{lut_code(target_brother_name + "12345")}
{target_birthday + "12345"}
{target_city + "12345"}
{lut_code(target_company_name + "12345")}
{lut_code(target_first_pet + "12345")}
{lut_code(target_second_pet + "12345")}
{lut_code(targets_gf_bf_first_name + "12345")}
{lut_code(targets_gf_bf_second_name + "12345")}
{lut_code(targets_gf_bf_surname + "12345")}
{group2(target_first_name + "12345")}
{group2(target_second_name + "12345")}
{group2(target_surname + "12345")}
{group2(target_father_name + "12345")}
{group2(target_mother_name + "12345")}
{group2(target_sister_name + "12345")}
{group2(target_brother_name + "12345")}
{group2(target_birthday + "12345")}
{group2(target_city + "12345")}
{group2(target_company_name + "12345")}
{group2(target_first_pet + "12345")}
{group2(target_second_pet + "12345")}
{group2(targets_gf_bf_first_name + "12345")}
{group2(targets_gf_bf_second_name + "12345")}
{group2(targets_gf_bf_surname + "12345")}
{group2rev(target_first_name + "12345")}
{group2rev(target_second_name + "12345")}
{group2rev(target_surname + "12345")}
{group2rev(target_father_name + "12345")}
{group2rev(target_mother_name + "12345")}
{group2rev(target_sister_name + "12345")}
{group2rev(target_brother_name + "12345")}
{group2rev(target_birthday + "12345")}
{group2rev(target_city + "12345")}
{group2rev(target_company_name + "12345")}
{group2rev(target_first_pet + "12345")}
{group2rev(target_second_pet + "12345")}
{group2rev(targets_gf_bf_first_name + "12345")}
{group2rev(targets_gf_bf_second_name + "12345")}
{group2rev(targets_gf_bf_surname + "12345")}
{lut_code(target_first_name + "123")}
{lut_code(target_second_name + "123")}
{lut_code(target_surname + "123")}
{lut_code(target_father_name + "123")}
{lut_code(target_mother_name + "123")}
{lut_code(target_sister_name + "123")}
{lut_code(target_brother_name + "123")}
{target_birthday + "123"}
{target_city + "123"}
{lut_code(target_company_name + "123")}
{lut_code(target_first_pet + "123")}
{lut_code(target_second_pet + "123")}
{lut_code(targets_gf_bf_first_name + "123")}
{lut_code(targets_gf_bf_second_name + "123")}
{lut_code(targets_gf_bf_surname + "123")}
{group2rev(target_first_name + "123")}
{group2rev(target_second_name + "123")}
{group2rev(target_surname + "123")}
{group2rev(target_father_name + "123")}
{group2rev(target_mother_name + "123")}
{group2rev(target_sister_name + "123")}
{group2rev(target_brother_name + "123")}
{group2rev(target_birthday + "123")}
{group2rev(target_city + "123")}
{group2rev(target_company_name + "123")}
{group2rev(target_first_pet + "123")}
{group2rev(target_second_pet + "123")}
{group2rev(targets_gf_bf_first_name + "123")}
{group2rev(targets_gf_bf_second_name + "123")}
{group2rev(targets_gf_bf_surname + "123")}
"""

        for i in range(0,100000):
            try:
                if "0" in add_keyword[i] or "1" in add_keyword[i] or "2" in add_keyword[i] or "3" in add_keyword[i] or "4" in add_keyword[i] or "5" in add_keyword[i] or "6" in add_keyword[i] or "7" in add_keyword[i] or "8" in add_keyword[i] or "9" in add_keyword[i]:
                    file_context = file_context + add_keyword[i] + "\n"

                else:
                    file_context = file_context + lut_code(add_keyword[i]) + "\n"
            except IndexError:
                pass

        words_last_version = ""

        file_context_last = file_context.split("\n")
        for i in range(0,100000):
            try:
                if file_context_last[i] == "\n" or file_context_last[i] == "":
                    pass
                else:
                    words_last_version = words_last_version + str(file_context_last[i]) + "\n"
            except IndexError:
                pass

        write_file = open("wordlist.txt","w",encoding="utf-8")
        write_file.write(words_last_version)
        
        colorprint("Created as wordlist.txt file","3")

    except FileExistsError:
        print(f"\n{colorprint('[ERROR]',1)} {colorprint('wordlist.txt',3)} already exists!\n")
        exit()

username = colorprint("@th3-iv4r",1)
welcome_text = f"\nWelcome wordlist-generator! Created by {str(username)}.\n"

print(welcome_text)
main_code()
