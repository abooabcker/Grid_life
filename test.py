from grid import grid_life
def test_grid():
    grid=grid_life([[1,1],[1,1]])
    assert grid.s==2
def test_is_alive():
    grid=grid_life([[1,1],[0,0]])
    assert grid.is_alive(0,0)==True
def test_num_neighboours():
    grid=grid_life([[1,1,0],[1,0,0],[1,1,1]])
    assert grid.num_neighbours(1,1)==6
    assert grid.num_neighbours(0,0)==3
def test_apply_rules():
    grid=grid_life([[1,0,1],[1,1,1],[0,0,1]])
    assert grid.apply_rules()==([[1,0,1],[1,0,1],[0,0,1]])
#def test_printer():

