# A program that enables to solve a Rubik's Cube
import sys


def rotation_u(sol):
    """Rotate the upper face clockwise."""
    global cube_face, cube_left, cube_back, cube_right, cube_up

    fc, lc, bc, rc, uc = cube_face.copy(), cube_left.copy(), cube_back.copy(), cube_right.copy(), cube_up.copy()
    cube_face[:3] = rc[:3]
    cube_left[:3] = fc[:3]
    cube_back[:3] = lc[:3]
    cube_right[:3] = bc[:3]

    up_only_clockwise()

    sol.append('U')


def rotation_ui(sol):
    """Rotate the upper face anticlockwise."""
    global cube_face, cube_left, cube_back, cube_right, cube_up

    fc, lc, bc, rc = cube_face.copy(), cube_left.copy(), cube_back.copy(), cube_right.copy()
    cube_face[:3] = lc[:3]
    cube_left[:3] = bc[:3]
    cube_back[:3] = rc[:3]
    cube_right[:3] = fc[:3]

    up_only_anticlockwise()

    sol.append('Ui')


def rotation_r(sol):
    """Rotate the right face clockwise."""
    global cube_face, cube_up, cube_back, cube_down, cube_right

    fc, uc, bc, dc, rc = cube_face.copy(), cube_up.copy(), cube_back.copy(), cube_down.copy(), cube_right.copy()
    cube_face[2], cube_face[5], cube_face[8] = dc[2], dc[5], dc[8]
    cube_up[2], cube_up[5], cube_up[8] = fc[2], fc[5], fc[8]
    cube_back[6], cube_back[3], cube_back[0] = uc[2], uc[5], uc[8]
    cube_down[2], cube_down[5], cube_down[8] = bc[6], bc[3], bc[0]

    cube_right[0], cube_right[1], cube_right[2] = rc[6], rc[3], rc[0]
    cube_right[3], cube_right[4], cube_right[5] = rc[7], rc[4], rc[1]
    cube_right[6], cube_right[7], cube_right[8] = rc[8], rc[5], rc[2]

    sol.append('R')


def rotation_ri(sol):
    """Rotate the right face anticlockwise."""
    global cube_face, cube_up, cube_back, cube_down, cube_right

    fc, uc, bc, dc, rc = cube_face.copy(), cube_up.copy(), cube_back.copy(), cube_down.copy(), cube_right.copy()
    cube_face[2], cube_face[5], cube_face[8] = uc[2], uc[5], uc[8]
    cube_up[2], cube_up[5], cube_up[8] = bc[6], bc[3], bc[0]
    cube_back[6], cube_back[3], cube_back[0] = dc[2], dc[5], dc[8]
    cube_down[2], cube_down[5], cube_down[8] = fc[2], fc[5], fc[8]

    cube_right[0], cube_right[1], cube_right[2] = rc[2], rc[5], rc[8]
    cube_right[3], cube_right[4], cube_right[5] = rc[1], rc[4], rc[7]
    cube_right[6], cube_right[7], cube_right[8] = rc[0], rc[3], rc[6]

    sol.append('Ri')


def rotation_l(sol):
    """Rotate the left face clockwise."""
    global cube_face, cube_up, cube_back, cube_down, cube_left

    fc, uc, bc, dc, lc = cube_face.copy(), cube_up.copy(), cube_back.copy(), cube_down.copy(), cube_left.copy()
    cube_face[0], cube_face[3], cube_face[6] = uc[0], uc[3], uc[6]
    cube_up[6], cube_up[3], cube_up[0] = bc[2], bc[5], bc[8]
    cube_back[2], cube_back[5], cube_back[8] = dc[6], dc[3], dc[0]
    cube_down[0], cube_down[3], cube_down[6] = fc[0], fc[3], fc[6]

    cube_left[0], cube_left[1], cube_left[2] = lc[6], lc[3], lc[0]
    cube_left[3], cube_left[4], cube_left[5] = lc[7], lc[4], lc[1]
    cube_left[6], cube_left[7], cube_left[8] = lc[8], lc[5], lc[2]

    sol.append('L')


def rotation_li(sol):
    """Rotate the left face anticlockwise."""
    global cube_face, cube_up, cube_back, cube_down, cube_left

    fc, uc, bc, dc, lc = cube_face.copy(), cube_up.copy(), cube_back.copy(), cube_down.copy(), cube_left.copy()
    cube_face[0], cube_face[3], cube_face[6] = dc[0], dc[3], dc[6]
    cube_up[6], cube_up[3], cube_up[0] = fc[6], fc[3], fc[0]
    cube_back[2], cube_back[5], cube_back[8] = uc[6], uc[3], uc[0]
    cube_down[0], cube_down[3], cube_down[6] = bc[8], bc[5], bc[2]

    cube_left[0], cube_left[1], cube_left[2] = lc[2], lc[5], lc[8]
    cube_left[3], cube_left[4], cube_left[5] = lc[1], lc[4], lc[7]
    cube_left[6], cube_left[7], cube_left[8] = lc[0], lc[3], lc[6]

    sol.append('Li')


def rotation_f(sol):
    """Rotate front face clockwise."""
    global cube_left, cube_up, cube_right, cube_down, cube_face

    lc, uc, rc, dc, fc = cube_left.copy(), cube_up.copy(), cube_right.copy(), cube_down.copy(), cube_face.copy()
    cube_left[2], cube_left[5], cube_left[8] = dc[:3]
    cube_up[6:] = lc[8], lc[5], lc[2]
    cube_right[0], cube_right[3], cube_right[6] = uc[6:]
    cube_down[:3] = rc[6], rc[3], rc[0]

    cube_face[0], cube_face[1], cube_face[2] = fc[6], fc[3], fc[0]
    cube_face[3], cube_face[4], cube_face[5] = fc[7], fc[4], fc[1]
    cube_face[6], cube_face[7], cube_face[8] = fc[8], fc[5], fc[2]

    sol.append('F')


def rotation_fi(sol):
    """Rotate front face anticlockwise."""
    global cube_left, cube_up, cube_right, cube_down, cube_face

    lc, uc, rc, dc, fc = cube_left.copy(), cube_up.copy(), cube_right.copy(), cube_down.copy(), cube_face.copy()
    cube_left[8], cube_left[5], cube_left[2] = uc[6:]
    cube_up[6:] = rc[0], rc[3], rc[6]
    cube_right[6], cube_right[3], cube_right[0] = dc[:3]
    cube_down[:3] = lc[2], lc[5], lc[8]

    cube_face[0], cube_face[1], cube_face[2] = fc[2], fc[5], fc[8]
    cube_face[3], cube_face[4], cube_face[5] = fc[1], fc[4], fc[7]
    cube_face[6], cube_face[7], cube_face[8] = fc[0], fc[3], fc[6]

    sol.append('Fi')


def rotation_d(sol):
    """Rotate the down face clockwise."""
    global cube_face, cube_left, cube_back, cube_right, cube_down

    fc, lc, bc, rc, dc = cube_face.copy(), cube_left.copy(), cube_back.copy(), cube_right.copy(), cube_down.copy()
    cube_face[6:] = lc[6:]
    cube_left[6:] = bc[6:]
    cube_back[6:] = rc[6:]
    cube_right[6:] = fc[6:]

    down_only_clockwise()

    sol.append('D')


def rotation_di(sol):
    """Rotate the down face anticlockwise."""
    global cube_face, cube_left, cube_back, cube_right, cube_down

    fc, lc, bc, rc, dc = cube_face.copy(), cube_left.copy(), cube_back.copy(), cube_right.copy(), cube_down.copy()
    cube_face[6:] = rc[6:]
    cube_left[6:] = fc[6:]
    cube_back[6:] = lc[6:]
    cube_right[6:] = bc[6:]

    down_only_anticlockwise()

    sol.append('Di')


def center_only_clockwise():
    global cube_up, cube_down, cube_left, cube_right

    lc, uc, rc, dc = cube_left.copy(), cube_up.copy(), cube_right.copy(), cube_down.copy()
    cube_left[1], cube_left[4], cube_left[7] = dc[3:6]
    cube_up[3:6] = lc[7], lc[4], lc[1]
    cube_right[1], cube_right[4], cube_right[7] = uc[3:6]
    cube_down[3:6] = rc[7], rc[4], rc[1]


def up_only_clockwise():
    """Rotate upper face only clockwise."""
    global cube_up
    uc = cube_up.copy()
    cube_up[0], cube_up[1], cube_up[2] = uc[6], uc[3], uc[0]
    cube_up[3], cube_up[4], cube_up[5] = uc[7], uc[4], uc[1]
    cube_up[6], cube_up[7], cube_up[8] = uc[8], uc[5], uc[2]


def up_only_anticlockwise():
    """Rotate upper face only anticlockwise."""
    global cube_up
    uc = cube_up.copy()

    cube_up[0], cube_up[1], cube_up[2] = uc[2], uc[5], uc[8]
    cube_up[3], cube_up[4], cube_up[5] = uc[1], uc[4], uc[7]
    cube_up[6], cube_up[7], cube_up[8] = uc[0], uc[3], uc[6]


def down_only_clockwise():
    """Rotate down face only clockwise."""
    global cube_down
    dc = cube_down.copy()

    cube_down[0], cube_down[1], cube_down[2] = dc[6], dc[3], dc[0]
    cube_down[3], cube_down[4], cube_down[5] = dc[7], dc[4], dc[1]
    cube_down[6], cube_down[7], cube_down[8] = dc[8], dc[5], dc[2]


def down_only_anticlockwise():
    """Rotate down face only anticlockwise."""
    global cube_down
    dc = cube_down.copy()

    cube_down[0], cube_down[1], cube_down[2] = dc[2], dc[5], dc[8]
    cube_down[3], cube_down[4], cube_down[5] = dc[1], dc[4], dc[7]
    cube_down[6], cube_down[7], cube_down[8] = dc[0], dc[3], dc[6]


def swap_adj_edges(sol):
    """Swap adjacent edge pieces on the upper face to match them with their face color
    Two adjacent edge pieces are in correct position
    """
    # Algorithm R, U, Ri, U, R, U, U, Ri, U
    rotation_r(sol)
    rotation_u(sol)
    rotation_ri(sol)

    rotation_u(sol)
    rotation_r(sol)
    rotation_u(sol)

    rotation_u(sol)
    rotation_ri(sol)
    rotation_u(sol)


def number_color_check(face_colors, c_dict):
    """Check whether all colors are entered and are valid."""
    colors_list = [c for c_lis in face_colors for c in c_lis]

    # Check for invalid colors
    for s in colors_list:
        if s not in c_dict.keys():
            print(f"Invalid color '{s}' entered. Re-enter the face colors.\n")
            return False
        if colors_list.count(s) > 9:
            sys.exit(f'{c_dict[s]} tiles exceeds 9')

    return True


def corner_check(c_dict, corners):
    """Check for invalid corner pieces."""
    valid = True
    invalid_corners = []
    users_entered_corners = list(get_corner_pc().values())

    for c in users_entered_corners:
        if users_entered_corners.count(c) > 1 or len(c) < 3:
            sys.exit("\nInvalid corner pieces. Ensure all colors are entered correctly.")

        elif c not in corners:
            invalid_corners += [f"{c_dict[list(c)[0]], c_dict[list(c)[1]], c_dict[list(c)[2]]}"]
            valid = False

    # Not sure whether this block will ever execute.
    if not valid:
        if len(invalid_corners) == 1:
            sys.exit(f"Corner piece {','.join(invalid_corners)} is not a valid corner piece in a 3*3 cube.")
        elif len(invalid_corners) > 1:
            sys.exit(f"Corner pieces {' and '.join(invalid_corners)} are not valid corner pieces in a 3*3 cube.")


def edge_check(c_dict, edges):
    """Check for invalid edge pieces."""
    valid = True
    invalid_edges = []
    user_entered_edges = list(get_edge_pc().values())

    for e in user_entered_edges.copy():
        if user_entered_edges.count(e) > 1:
            sys.exit('\nInvalid edge pieces. Ensure all colors are entered correctly.')

        elif e not in edges:
            invalid_edges += [f"{c_dict[list(e)[0]], c_dict[list(e)[1]]}"]
            valid = False

    if not valid:
        if len(invalid_edges) == 1:
            sys.exit(f"Edge piece {','.join(invalid_edges)} is not a valid edge piece in a 3*3 cube.")
        elif len(invalid_edges) > 1:
            sys.exit(f"Edge pieces {' and '.join(invalid_edges)} are not valid edge pieces in a 3*3 cube.")


def color_map(face_colors):
    """Identify face color and orient as needed.
       Default orientation when Yellow and White are up or down"""
    global cube_up, cube_face, cube_right, cube_left, cube_down, cube_back

    for c in face_colors:
        if c[4] == 'W':
            cube_up = c
        elif c[4] == 'R':
            cube_face = c
        elif c[4] == 'G':
            cube_left = c
        elif c[4] == 'B':
            cube_right = c
        elif c[4] == 'Y':
            cube_down = c
        elif c[4] == 'O':
            cube_back = c


def other_states(up, face, sol, right='', turn=0) -> None:
    """
    Defines other states of the cube if faces are swapped
    """
    global cube_up, cube_down, cube_face, cube_back, cube_right, cube_left
    uc, dc, fc, bc, rc, lc = (cube_up.copy(), cube_down.copy(), cube_face.copy(),
                              cube_back.copy(), cube_right.copy(), cube_left.copy())
    # Makes Green, Blue or Orange the front face
    if up == 'W' and face == 'G' and turn == 0:
        cube_face, cube_back, cube_right, cube_left = lc, rc, fc, bc

        up_only_anticlockwise()
        down_only_clockwise()
        sol.append(['Make Green the face and White top.'])
    elif up == 'W' and face == 'B' and turn == 0:
        cube_face, cube_back, cube_right, cube_left = rc, lc, bc, fc

        up_only_clockwise()
        down_only_anticlockwise()
        sol.append(['Make Blue the face and White the top.'])
    elif up == 'W' and face == 'O' and turn == 0:
        cube_face, cube_back, cube_right, cube_left = bc, fc, lc, rc

        up_only_clockwise()
        up_only_clockwise()
        down_only_anticlockwise()
        down_only_anticlockwise()

        sol.append(['Make Orange the face and White the top.'])

    elif up == 'Y' and face == 'G' and turn == 0:
        cube_face, cube_back, cube_right, cube_left = rc, lc, bc, fc

        up_only_clockwise()
        down_only_anticlockwise()
        sol.append(['Make Green the face and Yellow top.'])
    elif up == 'Y' and face == 'B' and turn == 0:
        cube_face, cube_back, cube_right, cube_left = lc, rc, fc, bc

        up_only_anticlockwise()
        down_only_clockwise()
        sol.append(['Make Blue the face and Yellow the top.'])
    elif up == 'Y' and face == 'O' and turn == 0:
        cube_face, cube_back, cube_right, cube_left = bc, fc, lc, rc

        up_only_clockwise()
        up_only_clockwise()
        down_only_anticlockwise()
        down_only_anticlockwise()

        sol.append(['Make Orange the face and Yellow the top.'])

    # Takes back the front face to Red
    elif up == 'W' and right == 'R' and face == 'R' and turn == 0:
        # Green at face currently
        cube_face, cube_back, cube_right, cube_left = rc, lc, bc, fc

        up_only_clockwise()
        down_only_anticlockwise()
        sol.append(['Make Red the face and White the top.'])
    elif up == 'W' and right == 'O' and face == 'R' and turn == 0:
        # Blue at face currently.
        cube_face, cube_back, cube_right, cube_left = lc, rc, fc, bc

        up_only_anticlockwise()
        down_only_clockwise()
        sol.append(["Make Red the face and White the top."])
    elif up == 'W' and right == 'G' and face == 'R' and turn == 0:
        # Orange at face currently.
        cube_face, cube_back, cube_right, cube_left = bc, fc, lc, rc

        up_only_clockwise()
        up_only_clockwise()
        down_only_anticlockwise()
        down_only_anticlockwise()

        sol.append(['Make Red the face and White the top.'])

    elif up == 'Y' and right == 'O' and face == 'R' and turn == 0:
        # Green at face currently
        cube_face, cube_back, cube_right, cube_left = lc, rc, fc, bc

        up_only_anticlockwise()
        down_only_clockwise()
        sol.append(['Make Red the face and Yellow the top.'])
    elif up == 'Y' and right == 'R' and face == 'R' and turn == 0:
        # Blue at face currently.
        cube_face, cube_back, cube_right, cube_left = rc, lc, bc, fc

        up_only_clockwise()
        down_only_anticlockwise()
        sol.append(["Make Red the face and Yellow the top."])
    elif up == 'Y' and right == 'B' and face == 'R' and turn == 0:
        # Orange at face currently.
        cube_face, cube_back, cube_right, cube_left = bc, fc, lc, rc

        up_only_clockwise()
        up_only_clockwise()
        down_only_anticlockwise()
        down_only_anticlockwise()

        sol.append(['Make Red the face and Yellow the top.'])

    # Turn over the cube
    elif up == 'Y' and right == 'G' and face == 'R' and turn == 1:
        other_states('W', 'O', sol)
        rotation_fi(sol)
        rotation_fi(sol)
        other_states('W', 'R', sol, 'G')
        rotation_f(sol)
        rotation_f(sol)
        center_only_clockwise()
        center_only_clockwise()

        del sol[-6:]
        sol.append(['Make Yellow the top face and Red the front face.'])


def color_entry(c_dict) -> list[list[str]]:
    """Receives and validates user input."""
    print('COLOR ENTRY INSTRUCTIONS\n\n'
          '1. Start face color entry with the red center piece on the front face and white center piece in the top face'
          '\n2. Enter the yellow face while the red center piece is on the top face. \n'
          '3. Enter the colors starting from the top left corner of each face and end at the bottom right corner-\n')

    faces = []
    face_len = 1
    while face_len <= 6:
        face_input = list(input(f'Face {face_len}: ').upper().strip())
        if len(face_input) == 9:
            faces.append(face_input)
            if number_color_check(faces, c_dict) is False:
                faces.pop(-1)
            else:
                face_len += 1
        else:
            print(f'Each face contains 9 colored tiles. Re-enter Face {face_len} colors.\n')

    return faces


def get_edge_pc() -> dict:
    """Gets the edge pieces
    and returns them as a dictionary"""
    global cube_up, cube_down, cube_face, cube_back, cube_right, cube_left

    ed_psn = {1: {cube_up[1], cube_back[1]}, 2: {cube_up[3], cube_left[1]}, 3: {cube_up[5], cube_right[1]},
              4: {cube_up[7], cube_face[1]}, 5: {cube_face[3], cube_left[5]}, 6: {cube_face[5], cube_right[3]},
              7: {cube_back[5], cube_left[3]}, 8: {cube_back[3], cube_right[5]}, 9: {cube_face[7], cube_down[1]},
              10: {cube_left[7], cube_down[3]}, 11: {cube_right[7], cube_down[5]}, 12: {cube_back[7], cube_down[7]}}

    return ed_psn


def get_corner_pc() -> dict:
    """Gets the corner pieces
    and returns them as a tuple in order of 1st - 8th corner piece."""
    global cube_up, cube_down, cube_face, cube_back, cube_right, cube_left

    corner_pcs = {1: {cube_up[0], cube_left[0], cube_back[2]}, 2: {cube_up[2], cube_right[2], cube_back[0]},
                  3: {cube_up[6], cube_left[2], cube_face[0]}, 4: {cube_up[8], cube_right[0], cube_face[2]},
                  5: {cube_down[6], cube_left[6], cube_back[8]}, 6: {cube_down[8], cube_right[8], cube_back[6]},
                  7: {cube_down[0], cube_left[8], cube_face[6]}, 8: {cube_down[2], cube_right[6], cube_face[8]}}

    return corner_pcs


def corner_move(top, face, right, sol, lay='not_last') -> None:
    """Rotate a corner piece to its right position.
    Algorithm R', D', R, D
    Executes at function corner_solving()"""
    global cube_up, cube_face, cube_right
    if lay == 'not_last':
        while True:
            rotation_ri(sol)
            rotation_di(sol)
            rotation_r(sol)
            rotation_d(sol)

            if cube_up[8] == top and cube_face[2] == face and cube_right[0] == right:
                other_states(top, 'R', sol, right)
                break
            else:
                continue

    elif lay == 'last':
        while cube_up[8] != top:
            rotation_ri(sol)
            rotation_di(sol)
            rotation_r(sol)
            rotation_d(sol)

        other_states(top, 'R', sol, right)


def edge_solving(edges, sol, top='W') -> None:
    """Correctly solve the edge pieces
    Does the necessary rotations to ensure the edges are well-placed therefore completing the white cross."""
    global cube_up, cube_down, cube_face, cube_back, cube_right, cube_left
    layer01_k = [1, 2, 3, 4]

    if top == 'W':

        # Work out every edge piece of the white layer
        while True:
            ep = get_edge_pc()
            e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4],
                                                                 ep[5], ep[6], ep[7], ep[8],
                                                                 ep[9], ep[10], ep[11], ep[12])

            for k, v in edges.items():
                if e1 == v and k in layer01_k:
                    if k == 1:
                        continue
                    elif k == 2:
                        other_states('W', 'G', sol)
                        swap_adj_edges(sol)
                        other_states('W', 'R', sol, 'R')
                        break
                    elif k == 3:
                        other_states('W', 'O', sol)
                        swap_adj_edges(sol)
                        other_states('W', 'R', sol, 'G')
                        break
                    elif k == 4:
                        other_states('W', 'O', sol)
                        rotation_fi(sol)
                        rotation_ui(sol)
                        rotation_li(sol)
                        rotation_u(sol)
                        other_states('W', 'R', sol, 'G')
                        break
                elif e2 == v and k in layer01_k:
                    if k == 1:
                        other_states('W', 'G', sol)
                        swap_adj_edges(sol)
                        other_states('W', 'R', sol, 'R')
                        break
                    elif k == 2:
                        continue
                    elif k == 3:
                        rotation_l(sol)
                        rotation_u(sol)
                        rotation_u(sol)
                        rotation_li(sol)
                        rotation_ui(sol)
                        rotation_ui(sol)
                        break
                    elif k == 4:
                        swap_adj_edges(sol)
                        break
                elif e3 == v and k in layer01_k:
                    if k == 1:
                        other_states('W', 'O', sol)
                        swap_adj_edges(sol)
                        other_states('W', 'R', sol, 'G')
                        break
                    elif k == 2:
                        rotation_ri(sol)
                        rotation_ui(sol)
                        rotation_ui(sol)
                        rotation_r(sol)
                        rotation_u(sol)
                        rotation_u(sol)
                        break
                    elif k == 3:
                        continue
                    elif k == 4:
                        other_states('W', 'B', sol)
                        swap_adj_edges(sol)
                        other_states('W', 'R', sol, 'O')
                        break
                elif e4 == v and k in layer01_k:
                    if k == 1:
                        rotation_f(sol)
                        rotation_u(sol)
                        rotation_r(sol)
                        rotation_ui(sol)
                        break
                    elif k == 2:
                        swap_adj_edges(sol)
                        break
                    elif k == 3:
                        other_states('W', 'B', sol)
                        swap_adj_edges(sol)
                        other_states('W', 'R', sol, 'O')
                        break
                    elif k == 4:
                        continue
                elif e5 == v and k in layer01_k:
                    if k == 1:
                        rotation_ui(sol)
                        rotation_li(sol)
                        rotation_u(sol)
                        break
                    elif k == 2:
                        rotation_li(sol)
                        break
                    elif k == 3:
                        rotation_u(sol)
                        rotation_f(sol)
                        rotation_ui(sol)
                        break
                    elif k == 4:
                        rotation_f(sol)
                        break
                elif e6 == v and k in layer01_k:
                    if k == 1:
                        rotation_u(sol)
                        rotation_r(sol)
                        rotation_ui(sol)
                        break
                    elif k == 2:
                        rotation_ui(sol)
                        rotation_fi(sol)
                        rotation_u(sol)
                        break
                    elif k == 3:
                        rotation_r(sol)
                        break
                    elif k == 4:
                        rotation_fi(sol)
                        break
                elif e7 == v and k in layer01_k:
                    if k == 1:
                        other_states('W', 'O', sol)
                        rotation_fi(sol)
                        other_states('W', 'R', sol, 'G')
                        break
                    elif k == 2:
                        rotation_l(sol)
                        break
                    elif k == 3:
                        rotation_u(sol)
                        rotation_u(sol)
                        rotation_l(sol)
                        rotation_ui(sol)
                        rotation_ui(sol)
                        break
                    elif k == 4:
                        rotation_u(sol)
                        rotation_l(sol)
                        rotation_ui(sol)
                        break
                elif e8 == v and k in layer01_k:
                    if k == 1:
                        other_states('W', 'O', sol)
                        rotation_f(sol)
                        other_states('W', 'R', sol, 'G')
                        break
                    elif k == 2:
                        rotation_ui(sol)
                        rotation_ui(sol)
                        rotation_ri(sol)
                        rotation_u(sol)
                        rotation_u(sol)
                        break
                    elif k == 3:
                        rotation_ri(sol)
                        break
                    elif k == 4:
                        rotation_ui(sol)
                        rotation_ri(sol)
                        rotation_u(sol)
                        break
                elif e9 == v and k in layer01_k:
                    if k == 1:
                        other_states('W', 'O', sol)
                        rotation_di(sol)
                        rotation_di(sol)
                        rotation_fi(sol)
                        rotation_fi(sol)
                        other_states('W', 'R', sol, 'G')
                        break
                    elif k == 2:
                        rotation_di(sol)
                        rotation_li(sol)
                        rotation_li(sol)
                        rotation_li(sol)
                        break
                    elif k == 3:
                        rotation_d(sol)
                        rotation_r(sol)
                        rotation_r(sol)
                        break
                    elif k == 4:
                        rotation_f(sol)
                        rotation_f(sol)
                        break
                elif e10 == v and k in layer01_k:
                    if k == 1:
                        other_states('W', 'O', sol)
                        rotation_di(sol)
                        rotation_fi(sol)
                        rotation_fi(sol)
                        break
                    elif k == 2:
                        rotation_li(sol)
                        rotation_li(sol)
                        break
                    elif k == 3:
                        rotation_d(sol)
                        rotation_d(sol)
                        rotation_r(sol)
                        rotation_r(sol)
                        break
                    elif k == 4:
                        rotation_d(sol)
                        rotation_f(sol)
                        rotation_f(sol)
                        break
                elif e11 == v and k in layer01_k:
                    if k == 1:
                        other_states('W', 'O', sol)
                        rotation_d(sol)
                        rotation_f(sol)
                        rotation_f(sol)
                        other_states('W', 'R', sol, 'G')
                        break
                    elif k == 2:
                        rotation_di(sol)
                        rotation_di(sol)
                        rotation_li(sol)
                        rotation_li(sol)
                        break
                    elif k == 3:
                        rotation_r(sol)
                        rotation_r(sol)
                        break
                    elif k == 4:
                        rotation_di(sol)
                        rotation_f(sol)
                        rotation_f(sol)
                        break
                elif e12 == v and k in layer01_k:
                    if k == 1:
                        other_states('W', 'O', sol)
                        rotation_f(sol)
                        rotation_f(sol)
                        other_states('W', 'R', sol, 'G')
                        break
                    elif k == 2:
                        rotation_d(sol)
                        rotation_li(sol)
                        rotation_li(sol)
                        break
                    elif k == 3:
                        rotation_di(sol)
                        rotation_r(sol)
                        rotation_r(sol)
                        break
                    elif k == 4:
                        rotation_di(sol)
                        rotation_di(sol)
                        rotation_f(sol)
                        rotation_f(sol)
                        break

            if cube_face[4] == 'G':
                other_states('W', 'R', sol, 'R')
            elif cube_face[4] == 'B':
                other_states('W', 'R', sol, 'O')
            elif cube_face[4] == 'O':
                other_states('W', 'R', sol, 'G')

            ep = get_edge_pc()
            e1, e2, e3, e4 = ep[1], ep[2], ep[3], ep[4]
            if e1 == edges[1] and e2 == edges[2] and e3 == edges[3] and e4 == edges[4]:
                break
            else:
                continue

    elif top == 'Y':
        # Work out every top edge piece of the yellow layer
        while True:
            ep = get_edge_pc()
            e1, e2, e3, e4 = ep[1], ep[2], ep[3], ep[4]
            for k, v in edges.items():
                if e1 == v and k in layer01_k:
                    if k == 1:
                        continue
                    elif k == 2:
                        other_states('Y', 'B', sol)
                        swap_adj_edges(sol)
                        other_states('Y', 'R', sol, 'R')
                        break
                    elif k == 3:
                        other_states('Y', 'O', sol)
                        swap_adj_edges(sol)
                        other_states('Y', 'R', sol, 'B')
                        break
                    elif k == 4:
                        other_states('Y', 'O', sol)
                        swap_adj_edges(sol)
                        other_states('Y', 'R', sol, 'B')
                        break
                elif e2 == v and k in layer01_k:
                    if k == 1:
                        other_states('Y', 'B', sol)
                        swap_adj_edges(sol)
                        other_states('Y', 'R', sol, 'R')
                        break
                    elif k == 2:
                        continue
                    elif k == 3:
                        other_states('Y', 'B', sol)
                        swap_adj_edges(sol)
                        other_states('Y', 'R', sol, 'R')
                        break
                    elif k == 4:
                        swap_adj_edges(sol)
                        break
                elif e3 == v and k in layer01_k:
                    if k == 1:
                        other_states('Y', 'O', sol)
                        swap_adj_edges(sol)
                        other_states('Y', 'R', sol, 'B')
                        break
                    elif k == 2:
                        other_states('Y', 'G', sol)
                        swap_adj_edges(sol)
                        other_states('Y', 'R', sol, 'O')
                        break
                    elif k == 3:
                        continue
                    elif k == 4:
                        other_states('Y', 'G', sol)
                        swap_adj_edges(sol)
                        other_states('Y', 'R', sol, 'O')
                        break
                elif e4 == v and k in layer01_k:
                    if k == 1:
                        swap_adj_edges(sol)
                        break
                    elif k == 2:
                        swap_adj_edges(sol)
                        break
                    elif k == 3:
                        other_states('Y', 'G', sol)
                        swap_adj_edges(sol)
                        other_states('Y', 'R', sol, 'O')
                        break
                    elif k == 4:
                        continue

            if cube_face[4] == 'G':
                other_states('Y', 'R', sol, 'O')
            elif cube_face[4] == 'B':
                other_states('Y', 'R', sol, 'R')
            elif cube_face[4] == 'O':
                other_states('Y', 'R', sol, 'B')

            ep = get_edge_pc()
            e1, e2, e3, e4 = ep[1], ep[2], ep[3], ep[4]
            if e1 == edges[1] and e2 == edges[2] and e3 == edges[3] and e4 == edges[4]:
                break
            else:
                continue


def corner_solving(corners, sol) -> None:
    """Correctly solve the corner pieces.
    Does the necessary rotations to ensure the corners are well-placed therefore completing a layer(white)."""
    global cube_up, cube_down, cube_face, cube_back, cube_right, cube_left
    cp = get_corner_pc()
    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
    layer01_k = [1, 2, 3, 4]

    cOne, cTwo, cThree, cFour = ['W', 'G', 'O'], ['W', 'B', 'O'], ['W', 'G', 'R'], ['W', 'B', 'R']

    # Work out every corner piece of the white layer.
    while True:
        for k, v in corners.items():
            if c1 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    other_states('W', 'B', sol)
                    rotation_r(sol)
                    rotation_di(sol)
                    rotation_di(sol)
                    rotation_ri(sol)
                    rotation_d(sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    other_states('W', 'G', sol)
                    rotation_l(sol)
                    rotation_d(sol)
                    rotation_li(sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_li(sol)
                    rotation_d(sol)
                    rotation_l(sol)
                    rotation_d(sol)
                    rotation_d(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
            elif c2 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    rotation_r(sol)
                    rotation_d(sol)
                    rotation_ri(sol)
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    rotation_r(sol)
                    rotation_di(sol)
                    rotation_ri(sol)
                    rotation_di(sol)
                    rotation_di(sol)
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_r(sol)
                    rotation_di(sol)
                    rotation_ri(sol)
                    rotation_di(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
            elif c3 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    rotation_l(sol)
                    rotation_di(sol)
                    rotation_li(sol)
                    rotation_di(sol)
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    rotation_l(sol)
                    rotation_d(sol)
                    rotation_li(sol)
                    rotation_d(sol)
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_l(sol)
                    rotation_d(sol)
                    rotation_li(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
            elif c4 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    rotation_ri(sol)
                    rotation_di(sol)
                    rotation_r(sol)
                    rotation_di(sol)
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    rotation_ri(sol)
                    rotation_d(sol)
                    rotation_r(sol)
                    rotation_d(sol)
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    rotation_ri(sol)
                    rotation_di(sol)
                    rotation_r(sol)
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
            elif c5 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    rotation_di(sol)
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    rotation_d(sol)
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_d(sol)
                    rotation_d(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
            elif c6 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    rotation_d(sol)
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    rotation_di(sol)
                    rotation_di(sol)
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_di(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
            elif c7 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    rotation_di(sol)
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    rotation_d(sol)
                    rotation_d(sol)
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_d(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
            elif c8 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    rotation_di(sol)
                    rotation_di(sol)
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    rotation_d(sol)
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    rotation_di(sol)
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                    break

        if cube_face[4] == 'G':
            other_states('W', 'R', sol, 'R')
        elif cube_face[4] == 'B':
            other_states('W', 'R', sol, 'O')
        elif cube_face[4] == 'O':
            other_states('W', 'R', sol, 'G')

        if (cube_up[0] == cube_up[2] == cube_up[6] == cube_up[8] == 'W' and
                cube_left[0] == cube_left[2] == 'G' and cube_face[0] == cube_face[2] == 'R'
                and cube_right[0] == cube_right[2] == 'B' and cube_back[0] == cube_back[2] == 'O'):
            break
        else:
            continue


def edge_flip(sol) -> None:
    """Flips an edge piece"""
    global cube_up, cube_down, cube_left, cube_right, cube_face, cube_back

    rotation_f(sol)
    rotation_ui(sol)
    rotation_r(sol)
    rotation_u(sol)


def edge_to_left_mid(sol) -> None:
    """Swap edge piece on upper layer with one on middle layer.
    The middle layer edge piece is shared between the front face and the left face."""
    rotation_ui(sol)
    rotation_li(sol)
    rotation_u(sol)
    rotation_l(sol)
    rotation_u(sol)
    rotation_f(sol)
    rotation_ui(sol)
    rotation_fi(sol)


def edge_to_right_mid(sol):
    """Swap edge piece on upper layer with one on middle layer.
    The middle layer edge piece is shared between the front and the right face."""
    rotation_u(sol)
    rotation_r(sol)
    rotation_ui(sol)
    rotation_ri(sol)
    rotation_ui(sol)
    rotation_fi(sol)
    rotation_u(sol)
    rotation_f(sol)


def solve_mid_layer(edges, sol):
    """Solve the middle layer, matching all the colors."""
    while True:
        ep = get_edge_pc()
        if 'Y' not in ep[1]:
            to_swap = cube_back[1]
            if to_swap == 'G':
                rotation_u(sol)
                if ep[1] == {'G', 'O'}:
                    other_states('Y', 'G', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'O')
                elif ep[1] == {'G', 'R'}:
                    other_states('Y', 'G', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'O')
            elif to_swap == 'R':
                rotation_u(sol)
                rotation_u(sol)
                if ep[1] == {'R', 'G'}:
                    edge_to_right_mid(sol)
                elif ep[1] == {'R', 'B'}:
                    edge_to_left_mid(sol)
            elif to_swap == 'B':
                rotation_ui(sol)
                if ep[1] == {'B', 'R'}:
                    other_states('Y', 'B', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'R')
                elif ep[1] == {'B', 'O'}:
                    other_states('Y', 'B', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'R')
            elif to_swap == 'O':
                if ep[1] == {'O', 'B'}:
                    other_states('Y', 'O', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'B')
                elif ep[1] == {'O', 'G'}:
                    other_states('Y', 'O', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'B')
        elif 'Y' not in ep[2]:
            to_swap = cube_left[1]
            if to_swap == 'G':
                rotation_ui(sol)
                rotation_ui(sol)
                if ep[2] == {'G', 'O'}:
                    other_states('Y', 'G', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'O')
                elif ep[2] == {'G', 'R'}:
                    other_states('Y', 'G', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'O')
            elif to_swap == 'R':
                rotation_ui(sol)
                if ep[2] == {'R', 'G'}:
                    edge_to_right_mid(sol)
                elif ep[2] == {'R', 'B'}:
                    edge_to_left_mid(sol)
            elif to_swap == 'B':
                if ep[2] == {'B', 'R'}:
                    other_states('Y', 'B', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'R')
                elif ep[2] == {'B', 'O'}:
                    other_states('Y', 'B', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'R')
            elif to_swap == 'O':
                rotation_u(sol)
                if ep[2] == {'O', 'B'}:
                    other_states('Y', 'O', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'B')
                elif ep[2] == {'O', 'G'}:
                    other_states('Y', 'O', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'B')
        elif 'Y' not in ep[3]:
            to_swap = cube_right[1]
            if to_swap == 'G':
                if ep[3] == {'G', 'O'}:
                    other_states('Y', 'G', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'O')
                elif ep[3] == {'G', 'R'}:
                    other_states('Y', 'G', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'O')
            elif to_swap == 'R':
                rotation_u(sol)
                if ep[3] == {'R', 'G'}:
                    edge_to_right_mid(sol)
                elif ep[3] == {'R', 'B'}:
                    edge_to_left_mid(sol)
            elif to_swap == 'B':
                rotation_u(sol)
                rotation_u(sol)
                if ep[3] == {'B', 'R'}:
                    other_states('Y', 'B', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'R')
                elif ep[3] == {'B', 'O'}:
                    other_states('Y', 'B', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'R')
            elif to_swap == 'O':
                rotation_ui(sol)
                if ep[3] == {'O', 'B'}:
                    other_states('Y', 'O', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'B')
                elif ep[3] == {'O', 'G'}:
                    other_states('Y', 'O', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'B')
        elif 'Y' not in ep[4]:
            to_swap = cube_face[1]
            if to_swap == 'G':
                rotation_ui(sol)
                if ep[4] == {'G', 'O'}:
                    other_states('Y', 'G', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'O')
                elif ep[4] == {'G', 'R'}:
                    other_states('Y', 'G', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'O')
            elif to_swap == 'R':
                if ep[4] == {'R', 'G'}:
                    edge_to_right_mid(sol)
                elif ep[4] == {'R', 'B'}:
                    edge_to_left_mid(sol)
            elif to_swap == 'B':
                rotation_u(sol)
                if ep[4] == {'B', 'R'}:
                    other_states('Y', 'B', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'R')
                elif ep[4] == {'B', 'O'}:
                    other_states('Y', 'B', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'R')
            elif to_swap == 'O':
                rotation_u(sol)
                rotation_u(sol)
                if ep[4] == {'O', 'B'}:
                    other_states('Y', 'O', sol)
                    edge_to_right_mid(sol)
                    other_states('Y', 'R', sol, 'B')
                elif ep[4] == {'O', 'G'}:
                    other_states('Y', 'O', sol)
                    edge_to_left_mid(sol)
                    other_states('Y', 'R', sol, 'B')

        ep = get_edge_pc()
        edg_pcs = [edges[1], edges[2], edges[3], edges[4]]
        if ep[1] in edg_pcs and ep[2] in edg_pcs and ep[3] in edg_pcs and ep[4] in edg_pcs:
            break
        else:
            continue

    if ((cube_face[3] == 'B' and cube_left[5] == 'R') or (cube_face[3] == 'R' and cube_left[5] == 'G')
            or (cube_face[3] == 'G' and cube_left[5] == 'R') or (cube_face[3] == 'G' and cube_left[5] == 'O')
            or (cube_face[3] == 'O' and cube_left[5] == 'G') or (cube_face[3] == 'B' and cube_left[5] == 'O')
            or (cube_face[3] == 'O' and cube_left[5] == 'B')):
        edge_to_left_mid(sol)
        solve_mid_layer(edges, sol)

    elif ((cube_face[5] == 'G' and cube_right[3] == 'R') or (cube_face[5] == 'G' and cube_right[3] == 'O')
          or (cube_face[5] == 'O' and cube_right[3] == 'G') or (cube_face[5] == 'B' and cube_right[3] == 'R')
          or (cube_face[5] == 'R' and cube_right[3] == 'B') or (cube_face[5] == 'B' and cube_right[3] == 'O')
          or (cube_face[5] == 'O' and cube_right[3] == 'B')):
        edge_to_right_mid(sol)
        solve_mid_layer(edges, sol)

    elif ((cube_left[3] == 'O' and cube_back[5] == 'B') or (cube_left[3] == 'G' and cube_back[5] == 'R')
          or (cube_left[3] == 'R' and cube_back[5] == 'G') or (cube_left[3] == 'O' and cube_back[5] == 'G')
          or (cube_left[3] == 'G' and cube_back[5] == 'O') or (cube_left[3] == 'R' and cube_back[5] == 'B')
          or (cube_left[3] == 'B' and cube_back[5] == 'R')):
        other_states('Y', 'B', sol)
        edge_to_left_mid(sol)
        other_states('Y', 'R', sol, right='R')
        solve_mid_layer(edges, sol)

    elif ((cube_right[5] == 'O' and cube_back[3] == 'G') or (cube_right[5] == 'R' and cube_back[3] == 'B')
          or (cube_right[5] == 'B' and cube_back[3] == 'R') or (cube_right[5] == 'O' and cube_back[3] == 'B')
          or (cube_right[5] == 'B' and cube_back[3] == 'O') or (cube_right[5] == 'R' and cube_back[3] == 'G')
          or (cube_right[5] == 'G' and cube_back[3] == 'R')):
        other_states('Y', 'G', sol)
        edge_to_right_mid(sol)
        other_states('Y', 'R', sol, right='O')
        solve_mid_layer(edges, sol)


def arrange_upper_corners(sol):
    """Moves corners in position 3, 1 in a clockwise way
    Corner 2 moves to 3 and 4 remains."""
    rotation_li(sol)
    rotation_u(sol)
    rotation_r(sol)
    rotation_ui(sol)
    rotation_l(sol)
    rotation_u(sol)
    rotation_ri(sol)
    rotation_ui(sol)


def solve_final_layer(edges, corners, sol):
    """Solve the final Yellow layer"""
    global cube_up, cube_face
    round_no = 1

    # Make Yellow cross on top face:
    if [cube_up[1], cube_up[3], cube_up[4], cube_up[5], cube_up[7]] != ['Y'] * 5:
        while True:
            # Check for a 3 consecutive Yellow tiles.
            if [cube_up[1], cube_up[4], cube_up[7]] == ['Y'] * 3:
                rotation_u(sol)
            if [cube_up[3], cube_up[4], cube_up[5]] == ['Y'] * 3:
                # Algorithm F, R, U ,Ri, Ui, Fi
                rotation_f(sol)
                rotation_r(sol)
                rotation_u(sol)
                rotation_ri(sol)
                rotation_ui(sol)
                rotation_fi(sol)
                break
            # Check for Yellow tiles forming an inverted L shape.
            elif [cube_up[1], cube_up[3], cube_up[4]] == ['Y'] * 3:
                # Algorithm F, U, R, Ui, Ri, Fi
                rotation_f(sol)
                rotation_u(sol)
                rotation_r(sol)
                rotation_ui(sol)
                rotation_ri(sol)
                rotation_fi(sol)
                break
            else:
                if round_no == 1:
                    other_states('Y', 'B', sol)
                    round_no += 1
                    continue
                elif round_no == 2:
                    other_states('Y', 'R', sol, 'R')
                    other_states('Y', 'G', sol)
                    round_no += 1
                    continue
                elif round_no == 3:
                    other_states('Y', 'R', sol, 'O')
                    other_states('Y', 'O', sol)
                    round_no += 1
                    continue
                elif round_no > 3:
                    other_states('Y', 'R', sol, 'B')
                    rotation_f(sol)
                    rotation_u(sol)
                    rotation_r(sol)
                    rotation_ui(sol)
                    rotation_ri(sol)
                    rotation_fi(sol)
                    round_no = 0
                    continue

    if cube_face[4] == 'G':
        other_states('Y', 'R', sol, 'O')
    elif cube_face[4] == 'B':
        other_states('Y', 'R', sol, 'R')
    elif cube_face[4] == 'O':
        other_states('Y', 'R', sol, 'B')

    # Ensure each edge piece is at its correct position
    edge_solving(edges, sol, 'Y')
    # Ensure each corner is at its correct position
    corner4 = {1: corners[1], 2: corners[2], 3: corners[3], 4: corners[4]}
    for k, v in corner4.items():
        cors = get_corner_pc()
        cp1, cp2, cp3, cp4 = cors[1], cors[2], cors[3], cors[4]
        if cp1 == v:
            if k == 1:
                other_states('Y', 'O', sol)
                cp3 = get_corner_pc()[3]
                while cp3 != {'Y', 'G', 'O'}:
                    arrange_upper_corners(sol)
                    cp3 = get_corner_pc()[3]
                other_states('Y', 'R', sol, 'B')
            elif k == 2:
                other_states('Y', 'B', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'R')
            elif k == 3:
                arrange_upper_corners(sol)
                arrange_upper_corners(sol)
            elif k == 4:
                other_states('Y', 'G', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'O')
        elif cp2 == v:
            if k == 1:
                other_states('Y', 'O', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'B')
                other_states('Y', 'B', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'R')
            elif k == 3:
                arrange_upper_corners(sol)
                other_states('Y', 'B', sol)
                cp3 = get_corner_pc()[3]
                while cp3 != {'Y', 'B', 'O'}:
                    arrange_upper_corners(sol)
                    cp3 = get_corner_pc()[3]
                other_states('Y', 'R', sol, 'R')
            elif k == 2:
                other_states('Y', 'G', sol)
                cp3 = get_corner_pc()[3]
                while cp3 != {'Y', 'G', 'R'}:
                    arrange_upper_corners(sol)
                    cp3 = get_corner_pc()[3]
                other_states('Y', 'R', sol, 'O')
            elif k == 4:
                other_states('Y', 'O', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'B')
                cp3 = get_corner_pc()[3]
                while cp3 != {'Y', 'B', 'R'}:
                    arrange_upper_corners(sol)
                    cp3 = get_corner_pc()[3]
        elif cp3 == v:
            if k == 1:
                arrange_upper_corners(sol)
                other_states('Y', 'O', sol)
                cp3 = get_corner_pc()[3]
                while cp3 != {'Y', 'G', 'O'}:
                    arrange_upper_corners(sol)
                    cp3 = get_corner_pc()[3]
                other_states('Y', 'R', sol, 'B')
            elif k == 2:
                arrange_upper_corners(sol)
                other_states('Y', 'B', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'R')
            elif k == 3:
                other_states('Y', 'B', sol)
                cp3 = get_corner_pc()[3]
                while cp3 != {'Y', 'B', 'O'}:
                    arrange_upper_corners(sol)
                    cp3 = get_corner_pc()[3]
                other_states('Y', 'R', sol, 'R')
            elif k == 4:
                arrange_upper_corners(sol)
                other_states('Y', 'G', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'O')
        elif cp4 == v:
            if k == 1:
                other_states('Y', 'B', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'R')
                other_states('Y', 'O', sol)
                cp3 = get_corner_pc()[3]
                while cp3 != {'Y', 'G', 'O'}:
                    arrange_upper_corners(sol)
                    cp3 = get_corner_pc()[3]
                other_states('Y', 'R', sol, 'B')
            elif k == 2:
                other_states('Y', 'G', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'O')
                other_states('Y', 'O', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'B')
            elif k == 3:
                other_states('Y', 'G', sol)
                arrange_upper_corners(sol)
                other_states('Y', 'R', sol, 'O')
                other_states('Y', 'B', sol)
                cp3 = get_corner_pc()[3]
                while cp3 != {'Y', 'B', 'O'}:
                    arrange_upper_corners(sol)
                    cp3 = get_corner_pc()[3]
                other_states('Y', 'R', sol, 'R')
            elif k == 4:
                cp3 = get_corner_pc()[3]
                while cp3 != {'Y', 'B', 'R'}:
                    arrange_upper_corners(sol)
                    cp3 = get_corner_pc()[3]

    if cube_face[4] == 'G':
        other_states('Y', 'R', sol, 'O')
    elif cube_face[4] == 'B':
        other_states('Y', 'R', sol, 'R')
    elif cube_face[4] == 'O':
        other_states('Y', 'R', sol, 'B')

    while True:
        corner_move('Y', 'R', 'G', sol, 'last')
        if cube_up[0] == cube_up[2] == 'Y' and cube_up[6] != 'Y':
            rotation_ui(sol)
        else:
            rotation_u(sol)

        if cube_face == ['R'] * 9 and cube_left == ['B'] * 9 and cube_right == ['G'] * 9 and cube_back == ['O'] * 9:
            sol.append(['<<< ALL DONE🎉>>>'])
            break
        else:
            continue


def make_white_cross(edges, sol):
    """Create a white cross at the top face(white)."""
    global cube_up
    # Bring white edges to their correct positions
    edge_solving(edges, sol, 'W')
    # Ensure the white edges are well oriented
    while True:
        if cube_up[1] != 'W':
            other_states('W', 'O', sol)
            edge_flip(sol)
            other_states('W', 'R', sol, 'G')
        elif cube_up[3] != 'W':
            other_states('W', 'G', sol)
            edge_flip(sol)
            other_states('W', 'R', sol, 'R')
        elif cube_up[5] != 'W':
            other_states('W', 'B', sol)
            edge_flip(sol)
            other_states('W', 'R', sol, 'O')
        elif cube_up[7] != 'W':
            edge_flip(sol)

        if cube_up[1] == 'W' and cube_up[3] == 'W' and cube_up[5] == 'W' and cube_up[7] == 'W':
            break
        else:
            continue


def proceed():
    """Allows the user to move to the next step."""
    trials = 0
    while True:
        decision = str(input("\nENTER 1 to proceed: ")).upper().strip()
        if decision == '1':
            return True
        elif trials == 5:
            sys.exit("You have exceeded the max trials allowed. Please follow the instructions given.")
        else:
            print("Please type Next or 1 to proceed.")
            trials += 1
            continue


def symbol_meaning(symbol):
    """Provides descriptive info on items in solution list."""

    to_do = ''
    if symbol == 'Ui':
        to_do = "Rotate the UP face ANTICLOCKWISE."
    elif symbol == 'U':
        to_do = "Rotate the UP face CLOCKWISE."
    elif symbol == 'R':
        to_do = "Rotate the RIGHT face CLOCKWISE."
    elif symbol == 'Ri':
        to_do = "Rotate the RIGHT face ANTICLOCKWISE."
    elif symbol == 'Di':
        to_do = "Rotate the DOWN face ANTICLOCKWISE."
    elif symbol == 'D':
        to_do = "Rotate the DOWN face CLOCKWISE."
    elif symbol == 'L':
        to_do = "Rotate the LEFT face CLOCKWISE."
    elif symbol == 'Li':
        to_do = "Rotate the LEFT face ANTICLOCKWISE."
    elif symbol == 'F':
        to_do = "Rotate the FRONT face CLOCKWISE."
    elif symbol == 'Fi':
        to_do = "Rotate the FRONT face ANTICLOCKWISE."

    return to_do


def results(sol):
    """Shows the steps to solve the cube."""

    step = 1
    moves = [i for i in sol if type(i) is str]

    start_stat = f"\nYou'll be able to solve the cube in {len(moves)} steps if you follow the steps keenly.\n"
    print(start_stat.center(len(start_stat) + 10), '-')
    for n in range(len(sol)):
        if sol[n] == ['<<< ALL DONE🎉>>>']:
            print(f"\n{sol[-1][0]}\n")
            break
        elif sol[n] != ['<<< ALL DONE🎉>>>'] and type(sol[n]) is list and type(sol[n + 1]) is list:
            del sol[n]
            if type(sol[n + 1]) is list:
                continue
            else:
                if proceed():
                    print(f"\n<<<{sol[n][0]}>>> \n")
        elif sol[n] != ['<<< ALL DONE🎉>>>'] and type(sol[n]) is list and type(sol[n + 1]) is not list:
            if proceed():
                print(f'\n<<<{sol[n][0]}>>> \n')
        else:
            if proceed():
                print(f"\nStep {step} <<<{symbol_meaning(sol[n])}>>>")
                step += 1


# Defines programs default parameters.
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

solution = []

COLOR_SIGNAGE = DEFAULTS['color symbols']
WHITE_CORNER_PCS = DEFAULTS['corner_ps white up']
YELLOW_CORNER_PCS = DEFAULTS['corner_ps yellow up']
EDGE_POSITIONS = DEFAULTS['edge pieces white up']
EDGE_POSITIONS2 = DEFAULTS['edge pieces yellow up']

cube_up, cube_face, cube_right, cube_left, cube_down, cube_back = [], [], [], [], [], []
cube_faces = color_entry(COLOR_SIGNAGE)

color_map(cube_faces)  # map user-entered data to correct cube faces
edge_check(COLOR_SIGNAGE, EDGE_POSITIONS.values())
corner_check(COLOR_SIGNAGE, WHITE_CORNER_PCS.values())

for num in range(2):
    if cube_up == ['W'] * 9:
        other_states('Y', 'R', solution, 'G', 1)
        # Solve the second layer
        solve_mid_layer(EDGE_POSITIONS2, solution)
        solve_final_layer(EDGE_POSITIONS2, YELLOW_CORNER_PCS, solution)
        results(solution)
        break
    else:
        # Verify edge and corner pieces
        make_white_cross(EDGE_POSITIONS, solution)
        corner_solving(WHITE_CORNER_PCS, solution)
