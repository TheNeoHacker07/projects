from main import is_palindrome,add_one




def test_answer():
    # оператор assert это встроенный оператор питона позваляюший отслеживать код,этот оператор принимает условие и необязательно сообщение,
     #которое выходит при исключении assertionerror
    

    #Assertion error выходит когда assert встречает false,если true,то ничего не произейдет


    assert add_one(5)==5