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

    fc, lc, bc, rc, uc = cube_face.copy(), cube_left.copy(), cube_back.copy(), cube_right.copy(), cube_up.copy()
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


def corner_check(up, down, left, right, face, back, c_dict, corners):
    """Check for invalid corner pieces."""
    valid = True
    invalid_corners = []
    users_entered_corners = ({up[0], left[0], back[2]}, {up[2], right[2], back[0]},
                             {up[6], left[2], face[0]}, {up[8], right[0], face[2]},
                             {down[0], left[8], face[6]}, {down[2], right[6], face[8]},
                             {down[6], left[6], back[8]}, {down[8], right[8], back[6]})

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


def edge_check(up, down, left, right, face, back, c_dict, edges):
    """Check for invalid edge pieces."""
    valid = True
    invalid_edges = []
    user_entered_edges = [{up[1], back[1]}, {up[3], left[1]}, {up[5], right[1]}, {up[7], face[1]},
                          {down[7], back[7]}, {down[3], left[7]}, {down[5], right[7]}, {down[1], face[7]},
                          {face[3], left[5]}, {face[5], right[3]}, {right[5], back[3]}, {back[5], left[3]}]

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


def color_map(face_colors, round_no):
    """Identify face color and orient as needed.
       Default orientation when Yellow and White are up or down"""
    global cube_up, cube_face, cube_right, cube_left, cube_down, cube_back

    for c in face_colors:
        if round_no is True:
            if c[4] == 'Y':
                cube_up = c
            elif c[4] == 'R':
                cube_face = c
            elif c[4] == 'B':
                cube_left = c
            elif c[4] == 'G':
                cube_right = c
            elif c[4] == 'W':
                cube_down = c
            elif c[4] == 'O':
                cube_back = c

        elif round_no is False:
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


def other_states(up, face, sol, right='') -> None:
    """
    Defines other states of the cube if faces are swapped
    """
    global cube_up, cube_down, cube_face, cube_back, cube_right, cube_left
    uc, dc, fc, bc, rc, lc = (cube_up.copy(), cube_down.copy(), cube_face.copy(),
                              cube_back.copy(), cube_right.copy(), cube_left.copy())
    # Green as face and white as up
    if up == 'W' and face == 'G':
        cube_face, cube_back, cube_right, cube_left = lc, rc, fc, bc

        up_only_anticlockwise()
        down_only_clockwise()
        sol.append(['Make Green the face and White top.'])

    # Blue as face and white as up
    elif up == 'W' and face == 'B':
        cube_face, cube_back, cube_right, cube_left = rc, lc, bc, fc

        up_only_clockwise()
        down_only_anticlockwise()
        sol.append(['Make Blue the face and White the top.'])

    # Orange as face and white as up
    elif up == 'W' and face == 'O':
        cube_face, cube_back, cube_right, cube_left = bc, fc, lc, rc

        up_only_clockwise()
        up_only_clockwise()
        down_only_anticlockwise()
        down_only_anticlockwise()

        sol.append(['Make Orange the face and White the top.'])

    # Following 3 statements makes Red the face while white remains up.
    elif up == 'W' and right == 'R' and face == 'R':
        # Green at face currently
        cube_face, cube_back, cube_right, cube_left = rc, lc, bc, fc

        up_only_clockwise()
        down_only_anticlockwise()
        sol.append(['Make Red the face and White the top.'])

    elif up == 'W' and right == 'O' and face == 'R':
        # Blue at face currently.
        cube_face, cube_back, cube_right, cube_left = lc, rc, fc, bc

        up_only_anticlockwise()
        down_only_clockwise()
        sol.append(["Make Red the face and White the top."])

    elif up == 'W' and right == 'G' and face == 'R':
        # Orange at face currently.
        cube_face, cube_back, cube_right, cube_left = bc, fc, lc, rc

        up_only_clockwise()
        up_only_clockwise()
        down_only_anticlockwise()
        down_only_anticlockwise()

        sol.append(['Make Red the face and White the top.'])

    # Turn the cube such that the yellow face is up and the white is down
    elif up == 'Y' and right == 'G' and face == 'R':
        pass


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


def side_fc_diffs(sf_diff, sol) -> tuple[list, list]:
    """Get face difference and the number of rotations required to an edge to its correct face."""

    global cube_up, cube_back, cube_left, cube_right, cube_face
    # Provide face difference to match the edge piece to it's corresponding face.
    if cube_up[1] == cube_up[3] == cube_up[5] == cube_up[7] == 'W':  # white cross
        matches = []
        side_fcs = [cube_back, cube_left, cube_face, cube_right]

        # Get color and its current face and the required position.
        for n in range(len(side_fcs)):
            face_dict = {'W': cube_up, 'Y': cube_down, 'G': cube_left, 'B': cube_right, 'R': cube_face, 'O': cube_back}
            matches += [[side_fcs[n][1], side_fcs[n][4], k] for k, v in face_dict.items() if side_fcs[n][1] == v[4]]

        # Get face difference (2 = 180 and 1/-1 = 90) in a list
        diff = [lis[1] + lis[2] for lis in matches]

        two_matches = []
        for k, v in sf_diff.items():
            # When no edge matches to it's face but requires only a face rotation to match them
            if diff[0] in v and diff[1] in v and diff[2] in v and diff[3] in v:
                if k == 1:
                    rotation_u(sol)
                    break
                elif k == -1:
                    rotation_ui(sol)
                    break
                elif k == 2:
                    rotation_u(sol)
                    rotation_u(sol)
                    break

            else:
                for i in diff:
                    if i in v:
                        two_matches.append(k)

        while cube_face[1] != 'R':
            rotation_u(sol)
            result = side_fc_diffs(sf_diff, sol)
            diff = result[0]
            two_matches = result[1]

        if two_matches == [2, 2]:
            swap_adj_edges(sol)
            result2 = side_fc_diffs(sf_diff, sol)
            diff = result2[0]
            two_matches = result2[1]
            return diff, two_matches
        else:
            return diff, two_matches


def get_edge_pc() -> dict:
    """Gets the edge pieces
    and returns them as a dictionary"""
    global cube_up, cube_down, cube_face, cube_back, cube_right, cube_left

    ed_psn = {1: {cube_up[1], cube_back[1]}, 2: {cube_up[3], cube_left[1]}, 3: {cube_up[5], cube_right[1]},
              4: {cube_up[7], cube_face[1]}, 5: {cube_face[3], cube_left[5]}, 6: {cube_face[5], cube_right[3]},
              7: {cube_back[5], cube_left[3]}, 8: {cube_back[3], cube_right[5]}, 9: {cube_face[7], cube_down[1]},
              10: {cube_left[7], cube_down[3]}, 11: {cube_right[7], cube_down[5]}, 12: {cube_back[7], cube_down[7]}}

    return ed_psn


def get_corner_pc() -> tuple:
    """Gets the corner pieces
    and returns them as a tuple in order of 1st - 8th corner piece."""
    global cube_up, cube_down, cube_face, cube_back, cube_right, cube_left

    # Get current position.
    corner_pc01, corner_pc02 = {cube_up[0], cube_left[0], cube_back[2]}, {cube_up[2], cube_right[2], cube_back[0]}
    corner_pc03, corner_pc04 = {cube_up[6], cube_left[2], cube_face[0]}, {cube_up[8], cube_right[0], cube_face[2]}
    corner_pc05, corner_pc06 = {cube_down[6], cube_left[6], cube_back[8]}, {cube_down[8], cube_right[8], cube_back[6]}
    corner_pc07, corner_pc08 = {cube_down[0], cube_left[8], cube_face[6]}, {cube_down[2], cube_right[6], cube_face[8]}

    return corner_pc01, corner_pc02, corner_pc03, corner_pc04, corner_pc05, corner_pc06, corner_pc07, corner_pc08


def corner_move(top, face, right, sol) -> None:
    """Rotate a corner piece to its right position.
    Algorithm R', D', R, D
    Executes at function corner_solving()"""
    global cube_up, cube_face, cube_right
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


def edge_solving(edges, sol):
    """Correctly solve the edge pieces
    Does the necessary rotations to ensure the edges are well-placed therefore completing the white cross."""
    global cube_up, cube_down, cube_face, cube_back, cube_right, cube_left
    ep = get_edge_pc()
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])

    layer01_k = [1, 2, 3, 4]

    # Work out every edge piece of the white layer
    while True:
        for k, v in edges.items():
            if e1 == v and k in layer01_k:
                if k == 1:
                    continue
                elif k == 2:
                    other_states('W', 'G', sol)
                    swap_adj_edges(sol)
                    other_states('W', 'R', sol, 'R')
                    ep = get_edge_pc()
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    other_states('W', 'O', sol)
                    swap_adj_edges(sol)
                    other_states('W', 'R', sol, 'G')
                    ep = get_edge_pc()
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    other_states('W', 'O', sol)
                    rotation_fi(sol)
                    rotation_ui(sol)
                    rotation_li(sol)
                    rotation_u(sol)
                    other_states('W', 'R', sol, 'G')
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
            elif e2 == v and k in layer01_k:
                if k == 1:
                    other_states('W', 'G', sol)
                    swap_adj_edges(sol)
                    other_states('W', 'R', sol, 'R')
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
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
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    swap_adj_edges(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
            elif e3 == v and k in layer01_k:
                if k == 1:
                    other_states('W', 'O', sol)
                    swap_adj_edges(sol)
                    other_states('W', 'R', sol, 'G')
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 2:
                    print('round 1')
                    rotation_ri(sol)
                    rotation_ui(sol)
                    rotation_ui(sol)
                    rotation_r(sol)
                    rotation_u(sol)
                    rotation_u(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    continue
                elif k == 4:
                    other_states('W', 'B', sol)
                    swap_adj_edges(sol)
                    other_states('W', 'R', sol, 'O')
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
            elif e4 == v and k in layer01_k:
                if k == 1:
                    rotation_f(sol)
                    rotation_u(sol)
                    rotation_r(sol)
                    rotation_ui(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 2:
                    swap_adj_edges(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    other_states('W', 'B', sol)
                    swap_adj_edges(sol)
                    other_states('W', 'R', sol, 'O')
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    continue
            elif e5 == v and k in layer01_k:
                if k == 1:
                    rotation_ui(sol)
                    rotation_li(sol)
                    rotation_u(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 2:
                    rotation_li(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    rotation_u(sol)
                    rotation_f(sol)
                    rotation_ui(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    rotation_f(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
            elif e6 == v and k in layer01_k:
                if k == 1:
                    rotation_u(sol)
                    rotation_r(sol)
                    rotation_ui(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 2:
                    rotation_ui(sol)
                    rotation_fi(sol)
                    rotation_u(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    rotation_r(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    rotation_fi(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
            elif e7 == v and k in layer01_k:
                if k == 1:
                    other_states('W', 'O', sol)
                    rotation_fi(sol)
                    other_states('W', 'R', sol, 'G')
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 2:
                    rotation_l(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    rotation_u(sol)
                    rotation_u(sol)
                    rotation_l(sol)
                    rotation_ui(sol)
                    rotation_ui(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    rotation_u(sol)
                    rotation_l(sol)
                    rotation_ui(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
            elif e8 == v and k in layer01_k:
                if k == 1:
                    other_states('W', 'O', sol)
                    rotation_f(sol)
                    other_states('W', 'R', sol, 'G')
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 2:
                    rotation_ui(sol)
                    rotation_ui(sol)
                    rotation_ri(sol)
                    rotation_u(sol)
                    rotation_u(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    rotation_ri(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    rotation_ui(sol)
                    rotation_ri(sol)
                    rotation_u(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
            elif e9 == v and k in layer01_k:
                if k == 1:
                    other_states('W', 'O', sol)
                    rotation_di(sol)
                    rotation_di(sol)
                    rotation_fi(sol)
                    rotation_fi(sol)
                    other_states('W', 'R', sol, 'G')
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 2:
                    rotation_di(sol)
                    rotation_li(sol)
                    rotation_li(sol)
                    rotation_li(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    rotation_d(sol)
                    rotation_r(sol)
                    rotation_r(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    rotation_f(sol)
                    rotation_f(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
            elif e10 == v and k in layer01_k:
                if k == 1:
                    other_states('W', 'O', sol)
                    rotation_di(sol)
                    rotation_fi(sol)
                    rotation_fi(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 2:
                    rotation_li(sol)
                    rotation_li(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    rotation_d(sol)
                    rotation_d(sol)
                    rotation_r(sol)
                    rotation_r(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    rotation_d(sol)
                    rotation_f(sol)
                    rotation_f(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
            elif e11 == v and k in layer01_k:
                if k == 1:
                    other_states('W', 'O', sol)
                    rotation_d(sol)
                    rotation_f(sol)
                    rotation_f(sol)
                    other_states('W', 'R', sol, 'G')
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 2:
                    rotation_di(sol)
                    rotation_di(sol)
                    rotation_li(sol)
                    rotation_li(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    rotation_r(sol)
                    rotation_r(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    rotation_di(sol)
                    rotation_f(sol)
                    rotation_f(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
            elif e12 == v and k in layer01_k:
                if k == 1:
                    other_states('W', 'O', sol)
                    rotation_f(sol)
                    rotation_f(sol)
                    other_states('W', 'R', sol, 'G')
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 2:
                    rotation_d(sol)
                    rotation_li(sol)
                    rotation_li(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 3:
                    rotation_di(sol)
                    rotation_r(sol)
                    rotation_r(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
                    break
                elif k == 4:
                    rotation_di(sol)
                    rotation_di(sol)
                    rotation_f(sol)
                    rotation_f(sol)
                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4], ep[5], ep[6],
                                                                         ep[7], ep[8], ep[9], ep[10], ep[11], ep[12])
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


def corner_solving(corners, sol):
    """Correctly solve the corner pieces.
    Does the necessary rotations to ensure the corners are well-placed therefore completing a layer(white)."""
    global cube_up, cube_down, cube_face, cube_back, cube_right, cube_left
    cp = get_corner_pc()
    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
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
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
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
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    other_states('W', 'G', sol)
                    rotation_l(sol)
                    rotation_d(sol)
                    rotation_li(sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_li(sol)
                    rotation_d(sol)
                    rotation_l(sol)
                    rotation_d(sol)
                    rotation_d(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
            elif c2 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    rotation_r(sol)
                    rotation_d(sol)
                    rotation_ri(sol)
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
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
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_r(sol)
                    rotation_di(sol)
                    rotation_ri(sol)
                    rotation_di(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
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
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    rotation_l(sol)
                    rotation_d(sol)
                    rotation_li(sol)
                    rotation_d(sol)
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_l(sol)
                    rotation_d(sol)
                    rotation_li(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
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
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    rotation_ri(sol)
                    rotation_d(sol)
                    rotation_r(sol)
                    rotation_d(sol)
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    rotation_ri(sol)
                    rotation_di(sol)
                    rotation_r(sol)
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
            elif c5 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    rotation_di(sol)
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    rotation_d(sol)
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_d(sol)
                    rotation_d(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
            elif c6 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    rotation_d(sol)
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    rotation_di(sol)
                    rotation_di(sol)
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_di(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
            elif c7 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    rotation_di(sol)
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    rotation_d(sol)
                    rotation_d(sol)
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    rotation_d(sol)
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
            elif c8 == v and k in layer01_k:
                if k == 1 and [cube_up[0], cube_left[0], cube_back[2]] != cOne:
                    rotation_di(sol)
                    rotation_di(sol)
                    other_states('W', 'O', sol)
                    corner_move('W', 'O', 'G', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 2 and [cube_up[2], cube_right[2], cube_back[0]] != cTwo:
                    rotation_d(sol)
                    other_states('W', 'B', sol)
                    corner_move('W', 'B', 'O', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 3 and [cube_up[6], cube_left[2], cube_face[0]] != cThree:
                    rotation_di(sol)
                    other_states('W', 'G', sol)
                    corner_move('W', 'G', 'R', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
                    break
                elif k == 4 and [cube_up[8], cube_right[0], cube_face[2]] != cFour:
                    corner_move('W', 'R', 'B', sol)
                    cp = get_corner_pc()
                    c1, c2, c3, c4, c5, c6, c7, c8 = cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]
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


def white_cross(up_fc_diff, sol):
    """
    Rotate faces till edges are on their correct faces.
    """
    # Rotate up face clockwise to match corresponding face
    two_matches = side_fc_diffs(up_fc_diff, sol)[1]

    # two adjacent colors matching
    for i in two_matches:
        if len(two_matches) > 2:
            if two_matches.count(i) == 2 and i == 2:
                rotation_u(sol)
                rotation_u(sol)
                break
            elif two_matches.count(i) == 2 and i == 1:
                rotation_u(sol)
                break
            elif two_matches.count(i) == 2 and i == -1:
                rotation_ui(sol)
                break

    diff = side_fc_diffs(up_fc_diff, sol)[0]
    center_piece = ''
    for i in diff:
        if i in up_fc_diff[1]:
            center_piece = i[0]

    if center_piece:
        other_states('W', center_piece, sol)
        swap_adj_edges(sol)
        if center_piece == 'G':
            other_states('W', 'R', sol, 'R')
        elif center_piece == 'O':
            other_states('W', 'R', sol, 'G')
        elif center_piece == 'B':
            other_states('W', 'R', sol, 'O')


def edge_flip(sol):
    """Flips an edge piece"""
    global cube_up, cube_down, cube_left, cube_right, cube_face, cube_back

    rotation_f(sol)
    rotation_ui(sol)
    rotation_r(sol)
    rotation_u(sol)


def make_white_cross(edges, sol):
    """Create a white cross at the top face(white)."""
    global cube_up
    # Bring white edges to their correct positions
    edge_solving(edges, sol)
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


# Defines programs default parameters.
defaults = {
    'color symbols': {'Y': 'Yellow', 'W': 'White', 'B': 'Blue', 'G': 'Green', 'R': 'Red', 'O': 'Orange'},
    'hor1 face difference': {2: ['OR', 'RO', 'GB', 'BG'],
                             1: ['RB', 'BO', 'OG', 'GR'],
                             -1: ['BR', 'RG', 'GO', 'OB']},
    'hor2 face difference': {2: ['OR', 'RO', 'GB', 'BG'],
                             -1: ['RB', 'BO', 'OG', 'GR'],
                             1: ['BR', 'RG', 'GO', 'OB']},
    'ver1 face difference': {2: [], 1: [], -1: []},
    'ver2 face difference': {2: [], 1: [], -1: []},
    'corner_ps white up': {1: {'G', 'O', 'W'}, 2: {'B', 'O', 'W'}, 3: {'G', 'R', 'W'}, 4: {'B', 'R', 'W'},
                           5: {'G', 'O', 'Y'}, 6: {'B', 'O', 'Y'}, 7: {'G', 'R', 'Y'}, 8: {'B', 'R', 'Y'}},
    'corner_ps yellow up': {1: {'B', 'O', 'Y'}, 2: {'G', 'O', 'Y'}, 3: {'B', 'R', 'Y'}, 4: {'G', 'R', 'Y'},
                            5: {'B', 'O', 'W'}, 6: {'G', 'O', 'W'}, 7: {'B', 'R', 'W'}, 8: {'G', 'R', 'W'}},
    'edge pieces': {1: {'W', 'O'}, 2: {'W', 'G'}, 3: {'W', 'B'}, 4: {'W', 'R'}, 5: {'R', 'G'}, 6: {'R', 'B'},
                    7: {'G', 'O'}, 8: {'O', 'B'}, 9: {'Y', 'R'}, 10: {'Y', 'G'}, 11: {'Y', 'B'}, 12: {'Y', 'O'}},
            }

solution = []

white_up_face_diffs = defaults['hor2 face difference']
yellow_up_face_diffs = defaults['hor1 face difference']
color_signage = defaults['color symbols']
edge_pieces = defaults['edge pieces'].values()
corner_pieces = defaults['corner_ps white up']
edge_positions = defaults['edge pieces']

cube_up, cube_face, cube_right, cube_left, cube_down, cube_back = [], [], [], [], [], []
cube_faces = color_entry(color_signage)

# Check if upper face(White) is done then set round_01 to True (make the yellow face the upper face)
if ['W'] * 9 in cube_faces:
    round_01 = True
    color_map(cube_faces, round_01)

    # Verify edge and corner pieces
    edge_check(cube_up, cube_down, cube_left, cube_right, cube_face, cube_back, color_signage, edge_pieces)
    corner_check(cube_up, cube_down, cube_left, cube_right, cube_face, cube_back, color_signage, corner_pieces.values())
else:
    round_01 = False  # Work with the lower face(white) first
    color_map(cube_faces, round_01)  # map user-entered data to correct cube faces

    # Verify edge and corner pieces
    edge_check(cube_up, cube_down, cube_left, cube_right, cube_face, cube_back, color_signage, edge_pieces)
    corner_check(cube_up, cube_down, cube_left, cube_right, cube_face, cube_back, color_signage, corner_pieces.values())

    make_white_cross(edge_positions, solution)
    white_cross(white_up_face_diffs, solution)
    corner_solving(corner_pieces, solution)


print(f"Solution {solution}\n")
print(f'UP {cube_up}')
print(f'FACE {cube_face}')
print(f'RIGHT {cube_right}')
print(f'LEFT {cube_left}')
print(f'DOWN {cube_down}')
print(f'BACK {cube_back}')
