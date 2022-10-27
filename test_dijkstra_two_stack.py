from algorithms import dijkstra_two_stack

def test_dijsktra_two_stack():

    expression_1 = "( ( 1 + 2 ) * 3 )"
    expression_2 = "( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )"

    assert dijkstra_two_stack(expression_1) == 9
    assert dijkstra_two_stack(expression_2) == 101

