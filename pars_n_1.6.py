import os
from lxml import etree


def getXMLdata(XML_path):
    try:

        tree = etree.parse(XML_path)  # загузка файла для парсинга
        root = tree.getroot()  # задается корневой элемент

        nsmap = {
            'default': "http://zakupki.gov.ru/oos/types/1",
            'ns2': "http://zakupki.gov.ru/oos/export/1",
            'ns3': "http://zakupki.gov.ru/oos/common/1",
            'ns4': 'http://zakupki.gov.ru/oos/base/1',
            'ns5': 'http://zakupki.gov.ru/oos/TPtypes/1',
            'ns6': "http://zakupki.gov.ru/oos/CPtypes/1",
            'ns7': "http://zakupki.gov.ru/oos/pprf615types/1",
            'ns8': "http://zakupki.gov.ru/oos/EPtypes/1",
            'ns9': "http://zakupki.gov.ru/oos/printform/1",
            'ns10': "http://zakupki.gov.ru/oos/control99/1"
        }

        # names_list = ["id", "externalId", "purchaseNumber", "directDate", "docPublishDate", "docNumber", "href"]
        # for name in names_list:
        #     dict = {".//default:" + name, ".//ns2:" + name, ".//ns3:" + name,
        #             ".//ns4:" + name, ".//ns5:" + name, ".//ns6:" + name,
        #             ".//ns7:" + name, ".//ns8:" + name, ".//ns9:" + name,
        #             ".//ns10:" + name}
        #     # print(name)
        #     for xpath in dict:
        #         elem = root.find(xpath, nsmap)  # в переменную elem загружаем найденное значение
        #         # print(elem)
        #         if elem is not None:      # поиск проиходит по очереди - если не найдено в одном ns, переходит в следующий
        #             element =(elem.text)  # как значение найдено оно передается в element
        #             print(element)
        #             break                 # и цикл завершается

        nodes_list = ["lot", "lot", "attachment"]
        v_name = ["fullName", "maxPrice", "url"]
        for name in nodes_list:
            # Словарь для поика значений в нодах XML-файла
            dict = {".//default:" + name, ".//ns2:" + name, ".//ns3:" + name,
                     ".//ns4:" + name, ".//ns5:" + name, ".//ns6:" + name,
                     ".//ns7:" + name, ".//ns8:" + name, ".//ns9:" + name,
                     ".//ns10:" + name}

            # Словарь для поика значений в именах  XML-файла
            v_dict = {".//default:" + v_name, ".//ns2:" + v_name, ".//ns3:" + v_name,
                       ".//ns4:" + v_name, ".//ns5:" + v_name, ".//ns6:" + v_name,
                       ".//ns7:" + v_name, ".//ns8:" + v_name, ".//ns9:" + v_name,
                       ".//ns10:" + v_name}

            for xpath in dict:
                elem = root.find(xpath, nsmap)  # в переменную elem загружаем найденное значение
                if elem is not None:      # поиск проиходит по очереди - если не найдено в одном ns, переходит в следующий
                    element =(elem)  # как значение найдено оно передается в element
                    break                 # и цикл завершается
            if elem is None:              # если элемент не был найден - выводиться ошибка
                print("Ошибка вывода элемента")

            for xpath2 in v_dict:
                v_elem = element.find(xpath2, nsmap)  # в переменную elem загружаем найденное значение
                if v_elem is not None:  # поиск проиходит по очереди - если не найдено в одном ns, переходит в следующий
                    v_element = (v_elem.text)  # как значение найдено оно передается в element
                    print(v_element)
                    break  # и цикл завершается
            if v_elem is None:  # если элемент не был найден - выводиться ошибка
                print("Ошибка вывода элемента")




        #Эталонная строка поиска в вложенных нодах
        # elem_v = root.find('.//default:lot', nsmap).find('.//default:fullName', nsmap)
        # print(elem_v.text)


    except IOError as e:
        print(e)


# Выбор файла парсинга без вызова цикла - для теста
getXMLdata("test.xml")        #Стандартная закупка
# getXMLdata("ml_1855739.xml")  # Многолот

# #берет файлы из папки с xml-файлами, и запускает цикл парсинга функцией getXMLdata          -НЕ УДАЛЯТЬ!!!!!!
# files_list = os.listdir('D:\\python\\test\ARH')
# for file in files_list:
#     getXMLdata(os.path.join(r'D:\python\test\ARH', file))


# Проверяем тип XML файла на соответсвие справочнику уведомлений (проведение/изменение/отмена)

# Типы файлов (первые буквы названий файлов) которые относятся к уведомлениям о !проведении закупки
###### версия строки для программы
##список извещений о проведении закупок
# set_list_isp = ['fcsNotificationEA', 'fcsNotificationEP', 'fcsNotificationINM', 'fcsNotificationOK',
#             'fcsNotificationPO', 'fcsNotificationZA', 'fcsNotificationZK', 'fcsNotificationZP',
#             'epNotificationEO', 'epNotificationEZ']
###### версия строки для программы

##список извещений о внесении изменений
# set_list_change = ['fcsnotificationEFDateChange', 'epProlongationEOK', 'epProlongationEOKOU', 'epProlongationEOKD', 'epProlongationEZK', 'fcsNotificationOrgChange', 'epNotificationCancelFailure', 'fcsPlacementResult']

##список извещений об отмене
# set_list_del = ['fcsNotificationCancel ', 'fcsNotificationCancelFailure ', 'epClarificationDoc', 'epClarificationResult', 'fcsNotificationLotCancel ', 'epNotificationCancel']

# set_list_isp = ['ml-_1855739.xml']
# set_list_change = ['ml3_1855739.xml']
# set_list_del = ['ml_1855739.xml']
#
# # Цикл проверки - сверяет типы файлов с названием обрабатываемого файла (в переменной XML_path)
# type_xml = ()
# for set1 in set_list_isp:
#     if XML_path.find(set1) >= 0:
#         # print(XML_path)
#         type_xml = ("Notification_isp")
# for set1 in set_list_change:
#     if XML_path.find(set1) >= 0:
#         # print(XML_path)
#         type_xml = ("Notification_change")
# for set1 in set_list_del:
#     if XML_path.find(set1) >= 0:
#         # print(XML_path)
#         type_xml = ("Notification_del")
# print(type_xml)    #Для отладки. потом убрать
