import sys
from project_modules import Cube

# Program default parameters.
DEFAULTS = {
    'color symbols': {'Y': 'Yellow', 'W': 'White', 'B': 'Blue', 'G': 'Green', 'R': 'Red', 'O': 'Orange'},
    'corner_ps white up': {1: {'G', 'O', 'W'}, 2: {'B', 'O', 'W'}, 3: {'G', 'R', 'W'}, 4: {'B', 'R', 'W'},
                           5: {'G', 'O', 'Y'}, 6: {'B', 'O', 'Y'}, 7: {'G', 'R', 'Y'}, 8: {'B', 'R', 'Y'}},
    'corner_ps yellow up': {1: {'B', 'O', 'Y'}, 2: {'G', 'O', 'Y'}, 3: {'B', 'R', 'Y'}, 4: {'G', 'R', 'Y'},
                            5: {'B', 'O', 'W'}, 6: {'G', 'O', 'W'}, 7: {'B', 'R', 'W'}, 8: {'G', 'R', 'W'}},
    'edge pieces white up': {1: {'W', 'O'}, 2: {'W', 'G'}, 3: {'W', 'B'}, 4: {'W', 'R'}, 5: {'R', 'G'}, 6: {'R', 'B'},
                             7: {'G', 'O'}, 8: {'O', 'B'}, 9: {'Y', 'R'}, 10: {'Y', 'G'}, 11: {'Y', 'B'},
                             12: {'Y', 'O'}},
    'edge pieces yellow up': {1: {'Y', 'O'}, 2: {'Y', 'B'}, 3: {'Y', 'G'}, 4: {'Y', 'R'}, 5: {'R', 'B'},
                              6: {'R', 'G'}, 7: {'O', 'B'}, 8: {'G', 'O'}, 9: {'W', 'R'}, 10: {'W', 'B'},
                              11: {'W', 'G'}, 12: {'W', 'O'}},
}

EDGES_WHITE_UP = DEFAULTS['edge pieces white up']
EDGES_YELLOW_UP = DEFAULTS['edge pieces yellow up']
CORNER_YELLOW_UP = DEFAULTS['corner_ps yellow up']
CORNER_WHITE_UP = DEFAULTS['corner_ps white up']
COLOR_DICTIONARY = DEFAULTS['color symbols']


def main(c_dict, epwu, cpwu, cpyu, epyu):
    cube = Cube(c_dict=c_dict,
                edge_pcs_white_up=epwu,
                edge_pcs_yellow_up=epyu,
                corner_pcs_yellow_up=cpyu,
                corner_pcs_white_up=cpwu)
    print('PAST HERE ')
    cube.color_map()
    cube.edge_check()
    cube.corner_check()

    for num in range(2):
        if (cube.cube_up == ['W'] * 9 and cube.cube_back == ['O'] * 9 and
                cube.cube_left == ['G'] * 9 and cube.cube_face == ['R'] * 9 and
                cube.cube_right == ['B'] * 9 and cube.cube_down == ['Y'] * 9):
            sys.exit('\n<<<THE CUBE IS ALREADY SOLVED>>>')
        elif (cube.cube_up == ['W'] * 9 and cube.cube_back[1] == 'O' and
              cube.cube_left[1] == 'G' and cube.cube_face[1] == 'R' and
              cube.cube_right[1] == 'B'):

            cube.other_states('Y', 'R', 'G', 1)
            # Solve the second layer
            cube.solve_mid_layer()
            cube.solve_final_layer()
            cube.results()
            break
        else:
            if cube.cube_up == ['W'] * 9:
                if (cube.cube_face[:3] == ['O'] * 3 and cube.cube_left[:3] == ['B'] * 3 and
                        cube.cube_right[:3] == ['G'] * 3 and cube.cube_back[:3] == ['R'] * 3):
                    cube.rotation_u()
                    cube.rotation_u()
                elif (cube.cube_face[:3] == ['B'] * 3 and cube.cube_left[:3] == ['R'] * 3 and
                      cube.cube_right[:3] == ['O'] * 3 and cube.cube_back[:3] == ['G'] * 3):
                    cube.rotation_ui()
                elif (cube.cube_face[:3] == ['G'] * 3 and cube.cube_left[:3] == ['O'] * 3 and
                      cube.cube_right[:3] == ['R'] * 3 and cube.cube_back[:3] == ['B'] * 3):
                    cube.rotation_u()
            else:
                # Verify edge and corner pieces
                cube.make_white_cross()
                cube.corner_solving()


if __name__ == "__main__":
    main(c_dict=COLOR_DICTIONARY, epwu=EDGES_WHITE_UP, epyu=EDGES_YELLOW_UP,
         cpwu=CORNER_WHITE_UP, cpyu=CORNER_YELLOW_UP)
