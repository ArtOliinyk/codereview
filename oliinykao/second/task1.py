"""
Вивести всі списки, що існуюють у головному списку
"""
def internal_lists(main_list):
    for element in main_list:
        if isinstance(element, list):
            print(element)
        
