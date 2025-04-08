"""This contains the functions used to solve the Rubik's cube"""

import sys
import functools
import logging


logging.basicConfig(level=logging.INFO,
                    filename="logfile.log", filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")


def log_function_call(func):
    """Log a function when it's called"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


class Cube:
    """Allows formatting of the output which allows the user to follow the steps in a human-readable manner."""

    def __init__(self, c_dict, edge_pcs_yellow_up, corner_pcs_yellow_up, edge_pcs_white_up, corner_pcs_white_up):

        self.solution = []
        self.cube_up = []
        self.cube_down = []
        self.cube_face = []
        self.cube_back = []
        self.cube_left = []
        self.cube_right = []

        self.valid_colors = c_dict
        self.edge_pcs_yellow_up = edge_pcs_yellow_up
        self.corner_pcs_yellow_up = corner_pcs_yellow_up
        self.edge_pcs_white_up = edge_pcs_white_up
        self.corner_pcs_white_up = corner_pcs_white_up
        self.corner_pcs_white_up_val = corner_pcs_white_up.values()
        self.edge_pcs_white_up_val = edge_pcs_white_up.values()

    def rotation_u(self):
        """Rotate the upper face clockwise."""

        fc, lc, bc = self.cube_face.copy(), self.cube_left.copy(), self.cube_back.copy()
        rc, uc = self.cube_right.copy(), self.cube_up.copy()
        self.cube_face[:3] = rc[:3]
        self.cube_left[:3] = fc[:3]
        self.cube_back[:3] = lc[:3]
        self.cube_right[:3] = bc[:3]

        self.up_only_clockwise()

        self.solution.append('U')

    def rotation_ui(self):
        """Rotate the upper face anticlockwise."""

        fc, lc, bc = self.cube_face.copy(), self.cube_left.copy(), self.cube_back.copy()
        rc = self.cube_right.copy()
        self.cube_face[:3] = lc[:3]
        self.cube_left[:3] = bc[:3]
        self.cube_back[:3] = rc[:3]
        self.cube_right[:3] = fc[:3]

        self.up_only_anticlockwise()

        self.solution.append('Ui')

    def rotation_r(self):
        """Rotate the right face clockwise."""

        fc, uc, bc = self.cube_face.copy(), self.cube_up.copy(), self.cube_back.copy()
        dc, rc = self.cube_down.copy(), self.cube_right.copy()
        self.cube_face[2], self.cube_face[5], self.cube_face[8] = dc[2], dc[5], dc[8]
        self.cube_up[2], self.cube_up[5], self.cube_up[8] = fc[2], fc[5], fc[8]
        self.cube_back[6], self.cube_back[3], self.cube_back[0] = uc[2], uc[5], uc[8]
        self.cube_down[2], self.cube_down[5], self.cube_down[8] = bc[6], bc[3], bc[0]

        self.cube_right[0], self.cube_right[1], self.cube_right[2] = rc[6], rc[3], rc[0]
        self.cube_right[3], self.cube_right[4], self.cube_right[5] = rc[7], rc[4], rc[1]
        self.cube_right[6], self.cube_right[7], self.cube_right[8] = rc[8], rc[5], rc[2]

        self.solution.append('R')

    def rotation_ri(self):
        """Rotate the right face anticlockwise."""

        fc, uc, bc = self.cube_face.copy(), self.cube_up.copy(), self.cube_back.copy()
        dc, rc = self.cube_down.copy(), self.cube_right.copy()
        self.cube_face[2], self.cube_face[5], self.cube_face[8] = uc[2], uc[5], uc[8]
        self.cube_up[2], self.cube_up[5], self.cube_up[8] = bc[6], bc[3], bc[0]
        self.cube_back[6], self.cube_back[3], self.cube_back[0] = dc[2], dc[5], dc[8]
        self.cube_down[2], self.cube_down[5], self.cube_down[8] = fc[2], fc[5], fc[8]

        self.cube_right[0], self.cube_right[1], self.cube_right[2] = rc[2], rc[5], rc[8]
        self.cube_right[3], self.cube_right[4], self.cube_right[5] = rc[1], rc[4], rc[7]
        self.cube_right[6], self.cube_right[7], self.cube_right[8] = rc[0], rc[3], rc[6]

        self.solution.append('Ri')

    def rotation_l(self):
        """Rotate the left face clockwise."""

        fc, uc, bc = self.cube_face.copy(), self.cube_up.copy(), self.cube_back.copy()
        dc, lc = self.cube_down.copy(), self.cube_left.copy()
        self.cube_face[0], self.cube_face[3], self.cube_face[6] = uc[0], uc[3], uc[6]
        self.cube_up[6], self.cube_up[3], self.cube_up[0] = bc[2], bc[5], bc[8]
        self.cube_back[2], self.cube_back[5], self.cube_back[8] = dc[6], dc[3], dc[0]
        self.cube_down[0], self.cube_down[3], self.cube_down[6] = fc[0], fc[3], fc[6]

        self.cube_left[0], self.cube_left[1], self.cube_left[2] = lc[6], lc[3], lc[0]
        self.cube_left[3], self.cube_left[4], self.cube_left[5] = lc[7], lc[4], lc[1]
        self.cube_left[6], self.cube_left[7], self.cube_left[8] = lc[8], lc[5], lc[2]

        self.solution.append('L')

    def rotation_li(self):
        """Rotate the left face anticlockwise."""

        fc, uc, bc = self.cube_face.copy(), self.cube_up.copy(), self.cube_back.copy()
        dc, lc = self.cube_down.copy(), self.cube_left.copy()
        self.cube_face[0], self.cube_face[3], self.cube_face[6] = dc[0], dc[3], dc[6]
        self.cube_up[6], self.cube_up[3], self.cube_up[0] = fc[6], fc[3], fc[0]
        self.cube_back[2], self.cube_back[5], self.cube_back[8] = uc[6], uc[3], uc[0]
        self.cube_down[0], self.cube_down[3], self.cube_down[6] = bc[8], bc[5], bc[2]

        self.cube_left[0], self.cube_left[1], self.cube_left[2] = lc[2], lc[5], lc[8]
        self.cube_left[3], self.cube_left[4], self.cube_left[5] = lc[1], lc[4], lc[7]
        self.cube_left[6], self.cube_left[7], self.cube_left[8] = lc[0], lc[3], lc[6]

        self.solution.append('Li')

    def rotation_f(self):
        """Rotate front face clockwise."""

        lc, uc, rc = self.cube_left.copy(), self.cube_up.copy(), self.cube_right.copy()
        dc, fc = self.cube_down.copy(), self.cube_face.copy()
        self.cube_left[2], self.cube_left[5], self.cube_left[8] = dc[:3]
        self.cube_up[6:] = lc[8], lc[5], lc[2]
        self.cube_right[0], self.cube_right[3], self.cube_right[6] = uc[6:]
        self.cube_down[:3] = rc[6], rc[3], rc[0]

        self.cube_face[0], self.cube_face[1], self.cube_face[2] = fc[6], fc[3], fc[0]
        self.cube_face[3], self.cube_face[4], self.cube_face[5] = fc[7], fc[4], fc[1]
        self.cube_face[6], self.cube_face[7], self.cube_face[8] = fc[8], fc[5], fc[2]

        self.solution.append('F')

    def rotation_fi(self):
        """Rotate front face anticlockwise."""

        lc, uc, rc = self.cube_left.copy(), self.cube_up.copy(), self.cube_right.copy()
        dc, fc = self.cube_down.copy(), self.cube_face.copy()
        self.cube_left[8], self.cube_left[5], self.cube_left[2] = uc[6:]
        self.cube_up[6:] = rc[0], rc[3], rc[6]
        self.cube_right[6], self.cube_right[3], self.cube_right[0] = dc[:3]
        self.cube_down[:3] = lc[2], lc[5], lc[8]

        self.cube_face[0], self.cube_face[1], self.cube_face[2] = fc[2], fc[5], fc[8]
        self.cube_face[3], self.cube_face[4], self.cube_face[5] = fc[1], fc[4], fc[7]
        self.cube_face[6], self.cube_face[7], self.cube_face[8] = fc[0], fc[3], fc[6]

        self.solution.append('Fi')

    def rotation_d(self):
        """Rotate the down face clockwise."""

        fc, lc, bc = self.cube_face.copy(), self.cube_left.copy(), self.cube_back.copy()
        rc, dc = self.cube_right.copy(), self.cube_down.copy()
        self.cube_face[6:] = lc[6:]
        self.cube_left[6:] = bc[6:]
        self.cube_back[6:] = rc[6:]
        self.cube_right[6:] = fc[6:]

        self.down_only_clockwise()

        self.solution.append('D')

    def rotation_di(self):
        """Rotate the down face anticlockwise."""

        fc, lc, bc = self.cube_face.copy(), self.cube_left.copy(), self.cube_back.copy()
        rc, dc = self.cube_right.copy(), self.cube_down.copy()
        self.cube_face[6:] = rc[6:]
        self.cube_left[6:] = fc[6:]
        self.cube_back[6:] = lc[6:]
        self.cube_right[6:] = bc[6:]

        self.down_only_anticlockwise()

        self.solution.append('Di')

    def up_only_clockwise(self):
        """Rotate upper face only clockwise."""

        uc = self.cube_up.copy()
        self.cube_up[0], self.cube_up[1], self.cube_up[2] = uc[6], uc[3], uc[0]
        self.cube_up[3], self.cube_up[4], self.cube_up[5] = uc[7], uc[4], uc[1]
        self.cube_up[6], self.cube_up[7], self.cube_up[8] = uc[8], uc[5], uc[2]

    def up_only_anticlockwise(self):
        """Rotate upper face only anticlockwise."""

        uc = self.cube_up.copy()

        self.cube_up[0], self.cube_up[1], self.cube_up[2] = uc[2], uc[5], uc[8]
        self.cube_up[3], self.cube_up[4], self.cube_up[5] = uc[1], uc[4], uc[7]
        self.cube_up[6], self.cube_up[7], self.cube_up[8] = uc[0], uc[3], uc[6]

    def center_only_clockwise(self):
        """Rotates the vertical center face"""

        lc, uc, rc = self.cube_left.copy(), self.cube_up.copy(), self.cube_right.copy()
        dc = self.cube_down.copy()
        self.cube_left[1], self.cube_left[4], self.cube_left[7] = dc[3:6]
        self.cube_up[3:6] = lc[7], lc[4], lc[1]
        self.cube_right[1], self.cube_right[4], self.cube_right[7] = uc[3:6]
        self.cube_down[3:6] = rc[7], rc[4], rc[1]

    def down_only_clockwise(self):
        """Rotate down face only clockwise."""

        dc = self.cube_down.copy()

        self.cube_down[0], self.cube_down[1], self.cube_down[2] = dc[6], dc[3], dc[0]
        self.cube_down[3], self.cube_down[4], self.cube_down[5] = dc[7], dc[4], dc[1]
        self.cube_down[6], self.cube_down[7], self.cube_down[8] = dc[8], dc[5], dc[2]

    def down_only_anticlockwise(self):
        """Rotate down face only anticlockwise."""

        dc = self.cube_down.copy()

        self.cube_down[0], self.cube_down[1], self.cube_down[2] = dc[2], dc[5], dc[8]
        self.cube_down[3], self.cube_down[4], self.cube_down[5] = dc[1], dc[4], dc[7]
        self.cube_down[6], self.cube_down[7], self.cube_down[8] = dc[0], dc[3], dc[6]

    @log_function_call
    def edge_check(self):
        """Check for invalid edge pieces."""
        valid = True
        invalid_edges = []
        user_entered_edges = list(self.get_edge_pc().values())

        for e in user_entered_edges.copy():
            if user_entered_edges.count(e) > 1:
                sys.exit('\nInvalid edge pieces. Ensure all colors are entered correctly.')

            elif e not in self.edge_pcs_white_up_val:
                invalid_edges += [f"{self.valid_colors[list(e)[0]], self.valid_colors[list(e)[1]]}"]
                valid = False

        # Will this block ever run? I'm not sure
        if not valid:
            if len(invalid_edges) == 1:
                sys.exit(f"Edge piece {','.join(invalid_edges)} is not a valid edge piece in a 3*3 cube.")
            elif len(invalid_edges) > 1:
                sys.exit(f"Edge pieces {' and '.join(invalid_edges)} are not valid edge pieces in a 3*3 cube.")

    @log_function_call
    def corner_check(self):
        """Check for invalid corner pieces."""
        valid = True
        invalid_corners = []
        users_entered_corners = list(self.get_corner_pc().values())

        for c in users_entered_corners:
            if users_entered_corners.count(c) > 1 or len(c) < 3:
                sys.exit("\nInvalid corner pieces. Ensure all colors are entered correctly.")

            elif c not in self.corner_pcs_white_up_val:
                invalid_corners += [f"{self.valid_colors[list(c)[0]], self.valid_colors[list(c)[1]],
                                    self.valid_colors[list(c)[2]]}"]
                valid = False

        # Not sure whether this block will ever execute.
        if not valid:
            if len(invalid_corners) == 1:
                sys.exit(f"Corner piece {','.join(invalid_corners)} is not a valid corner piece in a 3*3 cube.")
            elif len(invalid_corners) > 1:
                sys.exit(f"Corner pieces {' and '.join(invalid_corners)} are not valid corner pieces in a 3*3 cube.")

    @log_function_call
    def other_states(self, up, face, right='', turn=0) -> None:
        """
        Defines other states of the cube if faces are swapped
        """
        uc, dc, fc, bc, rc, lc = (self.cube_up.copy(), self.cube_down.copy(), self.cube_face.copy(),
                                  self.cube_back.copy(), self.cube_right.copy(), self.cube_left.copy())
        # Makes Green, Blue or Orange the front face
        if up == 'W' and face == 'G' and turn == 0:
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = lc, rc, fc, bc

            self.up_only_anticlockwise()
            self.down_only_clockwise()
            self.solution.append(['Make Green the face and White top.'])
        elif up == 'W' and face == 'B' and turn == 0:
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = rc, lc, bc, fc

            self.up_only_clockwise()
            self.down_only_anticlockwise()
            self.solution.append(['Make Blue the face and White the top.'])
        elif up == 'W' and face == 'O' and turn == 0:
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = bc, fc, lc, rc

            self.up_only_clockwise()
            self.up_only_clockwise()
            self.down_only_anticlockwise()
            self.down_only_anticlockwise()

            self.solution.append(['Make Orange the face and White the top.'])

        elif up == 'Y' and face == 'G' and turn == 0:
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = rc, lc, bc, fc

            self.up_only_clockwise()
            self.down_only_anticlockwise()
            self.solution.append(['Make Green the face and Yellow top.'])
        elif up == 'Y' and face == 'B' and turn == 0:
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = lc, rc, fc, bc

            self.up_only_anticlockwise()
            self.down_only_clockwise()
            self.solution.append(['Make Blue the face and Yellow the top.'])
        elif up == 'Y' and face == 'O' and turn == 0:
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = bc, fc, lc, rc

            self.up_only_clockwise()
            self.up_only_clockwise()
            self.down_only_anticlockwise()
            self.down_only_anticlockwise()

            self.solution.append(['Make Orange the face and Yellow the top.'])

        # Takes back the front face to Red
        elif up == 'W' and right == 'R' and face == 'R' and turn == 0:
            # Green at face currently
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = rc, lc, bc, fc

            self.up_only_clockwise()
            self.down_only_anticlockwise()
            self.solution.append(['Make Red the face and White the top.'])
        elif up == 'W' and right == 'O' and face == 'R' and turn == 0:
            # Blue at face currently.
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = lc, rc, fc, bc

            self.up_only_anticlockwise()
            self.down_only_clockwise()
            self.solution.append(["Make Red the face and White the top."])
        elif up == 'W' and right == 'G' and face == 'R' and turn == 0:
            # Orange at face currently.
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = bc, fc, lc, rc

            self.up_only_clockwise()
            self.up_only_clockwise()
            self.down_only_anticlockwise()
            self.down_only_anticlockwise()

            self.solution.append(['Make Red the face and White the top.'])

        elif up == 'Y' and right == 'O' and face == 'R' and turn == 0:
            # Green at face currently
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = lc, rc, fc, bc

            self.up_only_anticlockwise()
            self.down_only_clockwise()
            self.solution.append(['Make Red the face and Yellow the top.'])
        elif up == 'Y' and right == 'R' and face == 'R' and turn == 0:
            # Blue at face currently.
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = rc, lc, bc, fc

            self.up_only_clockwise()
            self.down_only_anticlockwise()
            self.solution.append(["Make Red the face and Yellow the top."])
        elif up == 'Y' and right == 'B' and face == 'R' and turn == 0:
            # Orange at face currently.
            self.cube_face, self.cube_back, self.cube_right, self.cube_left = bc, fc, lc, rc

            self.up_only_clockwise()
            self.up_only_clockwise()
            self.down_only_anticlockwise()
            self.down_only_anticlockwise()

            self.solution.append(['Make Red the face and Yellow the top.'])

        # Turn over the cube
        elif up == 'Y' and right == 'G' and face == 'R' and turn == 1:
            self.other_states('W', 'O')
            self.rotation_fi()
            self.rotation_fi()
            self.other_states('W', 'R', 'G')
            self.rotation_f()
            self.rotation_f()
            self.center_only_clockwise()
            self.center_only_clockwise()

            del self.solution[-6:]
            self.solution.append(['Make Yellow the top face and Red the front face.'])

    @log_function_call
    def solve_final_layer(self):
        """Solve the final Yellow layer"""
        round_no = 1

        # Make Yellow cross on top face:
        if [self.cube_up[1], self.cube_up[3], self.cube_up[4], self.cube_up[5], self.cube_up[7]] != ['Y'] * 5:
            while True:
                # Check for a 3 consecutive Yellow tiles.
                if [self.cube_up[1], self.cube_up[4], self.cube_up[7]] == ['Y'] * 3:
                    self.rotation_u()
                if [self.cube_up[3], self.cube_up[4], self.cube_up[5]] == ['Y'] * 3:
                    # Algorithm F, R, U ,Ri, Ui, Fi
                    self.rotation_f()
                    self.rotation_r()
                    self.rotation_u()
                    self.rotation_ri()
                    self.rotation_ui()
                    self.rotation_fi()
                    break
                # Check for Yellow tiles forming an inverted L shape.
                elif [self.cube_up[1], self.cube_up[3], self.cube_up[4]] == ['Y'] * 3:
                    # Algorithm F, U, R, Ui, Ri, Fi
                    self.rotation_f()
                    self.rotation_u()
                    self.rotation_r()
                    self.rotation_ui()
                    self.rotation_ri()
                    self.rotation_fi()
                    break
                else:
                    if round_no == 1:
                        self.other_states('Y', 'B')
                        round_no += 1
                        continue
                    elif round_no == 2:
                        self.other_states('Y', 'R', 'R')
                        self.other_states('Y', 'G')
                        round_no += 1
                        continue
                    elif round_no == 3:
                        self.other_states('Y', 'R', 'O')
                        self.other_states('Y', 'O')
                        round_no += 1
                        continue
                    elif round_no > 3:
                        self.other_states('Y', 'R', 'B')
                        self.rotation_f()
                        self.rotation_u()
                        self.rotation_r()
                        self.rotation_ui()
                        self.rotation_ri()
                        self.rotation_fi()
                        round_no = 0
                        continue

        # Ensure each edge piece is at its correct position
        self.edge_solving(self.edge_pcs_yellow_up, 'Y')
        # Ensure each corner is at its correct position
        corner4 = {1: self.corner_pcs_yellow_up[1], 2: self.corner_pcs_yellow_up[2], 3: self.corner_pcs_yellow_up[3],
                   4: self.corner_pcs_yellow_up[4]}
        for k, v in corner4.items():
            cors = self.get_corner_pc()
            cp1, cp2, cp3, cp4 = cors[1], cors[2], cors[3], cors[4]
            if cp1 == v:
                if k == 1:
                    self.other_states('Y', 'O')
                    cp3 = self.get_corner_pc()[3]
                    while cp3 != {'Y', 'G', 'O'}:
                        self.arrange_upper_corners()
                        cp3 = self.get_corner_pc()[3]
                    self.other_states('Y', 'R', 'B')
                elif k == 2:
                    self.other_states('Y', 'B')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'R')
                elif k == 3:
                    self.arrange_upper_corners()
                    self.arrange_upper_corners()
                elif k == 4:
                    self.other_states('Y', 'G')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'O')
            elif cp2 == v:
                if k == 1:
                    self.other_states('Y', 'O')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'B')
                    self.other_states('Y', 'B')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'R')
                elif k == 3:
                    self.arrange_upper_corners()
                    self.other_states('Y', 'B')
                    cp3 = self.get_corner_pc()[3]
                    while cp3 != {'Y', 'B', 'O'}:
                        self.arrange_upper_corners()
                        cp3 = self.get_corner_pc()[3]
                    self.other_states('Y', 'R', 'R')
                elif k == 2:
                    self.other_states('Y', 'G', )
                    cp3 = self.get_corner_pc()[3]
                    while cp3 != {'Y', 'G', 'R'}:
                        self.arrange_upper_corners()
                        cp3 = self.get_corner_pc()[3]
                    self.other_states('Y', 'R', 'O')
                elif k == 4:
                    self.other_states('Y', 'O')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'B')
                    cp3 = self.get_corner_pc()[3]
                    while cp3 != {'Y', 'B', 'R'}:
                        self.arrange_upper_corners()
                        cp3 = self.get_corner_pc()[3]
            elif cp3 == v:
                if k == 1:
                    self.arrange_upper_corners()
                    self.other_states('Y', 'O')
                    cp3 = self.get_corner_pc()[3]
                    while cp3 != {'Y', 'G', 'O'}:
                        self.arrange_upper_corners()
                        cp3 = self.get_corner_pc()[3]
                    self.other_states('Y', 'R''B')
                elif k == 2:
                    self.arrange_upper_corners()
                    self.other_states('Y', 'B')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'R')
                elif k == 3:
                    self.other_states('Y', 'B')
                    cp3 = self.get_corner_pc()[3]
                    while cp3 != {'Y', 'B', 'O'}:
                        self.arrange_upper_corners()
                        cp3 = self.get_corner_pc()[3]
                    self.other_states('Y', 'R', 'R')
                elif k == 4:
                    self.arrange_upper_corners()
                    self.other_states('Y', 'G')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'O')
            elif cp4 == v:
                if k == 1:
                    self.other_states('Y', 'B')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'R')
                    self.other_states('Y', 'O')
                    cp3 = self.get_corner_pc()[3]
                    while cp3 != {'Y', 'G', 'O'}:
                        self.arrange_upper_corners()
                        cp3 = self.get_corner_pc()[3]
                    self.other_states('Y', 'R', 'B')
                elif k == 2:
                    self.other_states('Y', 'G')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'O')
                    self.other_states('Y', 'O')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'B')
                elif k == 3:
                    self.other_states('Y', 'G')
                    self.arrange_upper_corners()
                    self.other_states('Y', 'R', 'O')
                    self.other_states('Y', 'B')
                    cp3 = self.get_corner_pc()[3]
                    while cp3 != {'Y', 'B', 'O'}:
                        self.arrange_upper_corners()
                        cp3 = self.get_corner_pc()[3]
                    self.other_states('Y', 'R', 'R')
                elif k == 4:
                    cp3 = self.get_corner_pc()[3]
                    while cp3 != {'Y', 'B', 'R'}:
                        self.arrange_upper_corners()
                        cp3 = self.get_corner_pc()[3]

        if self.cube_face[4] == 'G':
            self.other_states('Y', 'R', 'O')
        elif self.cube_face[4] == 'B':
            self.other_states('Y', 'R', 'R')
        elif self.cube_face[4] == 'O':
            self.other_states('Y', 'R', 'B')

        while True:
            self.corner_move('Y', 'R', 'G', 'last')
            if self.cube_up[0] == self.cube_up[2] == 'Y' and self.cube_up[6] != 'Y':
                self.rotation_ui()
            else:
                self.rotation_u()

            if (self.cube_face == ['R'] * 9 and self.cube_left == ['B'] * 9 and self.cube_right == ['G'] * 9 and
                    self.cube_back == ['O'] * 9):
                self.solution.append(['<<< ALL DONE🎉>>>'])
                break
            else:
                continue

    @log_function_call
    def get_corner_pc(self) -> dict:
        """Gets the corner pieces
        and returns them as a tuple in order of 1st - 8th corner piece."""
        corner_pcs = {1: {self.cube_up[0], self.cube_left[0], self.cube_back[2]},
                      2: {self.cube_up[2], self.cube_right[2], self.cube_back[0]},
                      3: {self.cube_up[6], self.cube_left[2], self.cube_face[0]},
                      4: {self.cube_up[8], self.cube_right[0], self.cube_face[2]},
                      5: {self.cube_down[6], self.cube_left[6], self.cube_back[8]},
                      6: {self.cube_down[8], self.cube_right[8], self.cube_back[6]},
                      7: {self.cube_down[0], self.cube_left[8], self.cube_face[6]},
                      8: {self.cube_down[2], self.cube_right[6], self.cube_face[8]}
                      }

        return corner_pcs

    @log_function_call
    def edge_flip(self) -> None:
        """Flips an edge piece"""

        self.rotation_f()
        self.rotation_ui()
        self.rotation_r()
        self.rotation_u()

    @log_function_call
    def get_edge_pc(self) -> dict:
        """Gets the edge pieces
        and returns them as a dictionary"""
        ed_psn = {1: {self.cube_up[1], self.cube_back[1]},
                  2: {self.cube_up[3], self.cube_left[1]}, 3: {self.cube_up[5], self.cube_right[1]},
                  4: {self.cube_up[7], self.cube_face[1]},
                  5: {self.cube_face[3], self.cube_left[5]}, 6: {self.cube_face[5], self.cube_right[3]},
                  7: {self.cube_back[5], self.cube_left[3]},
                  8: {self.cube_back[3], self.cube_right[5]}, 9: {self.cube_face[7], self.cube_down[1]},
                  10: {self.cube_left[7], self.cube_down[3]},
                  11: {self.cube_right[7], self.cube_down[5]}, 12: {self.cube_back[7], self.cube_down[7]}
                  }

        return ed_psn

    @log_function_call
    def edge_solving(self, edges, top='W') -> None:
        """Correctly solve the edge pieces
        Does the necessary rotations to ensure the edges are well-placed therefore completing the white cross."""
        layer01_k = [1, 2, 3, 4]
        if top == 'W':
            # Work out every edge piece of the white layer
            while True:
                ep = self.get_edge_pc()
                e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12 = (ep[1], ep[2], ep[3], ep[4],
                                                                     ep[5], ep[6], ep[7], ep[8],
                                                                     ep[9], ep[10], ep[11], ep[12])
                for k, v in edges.items():
                    if e1 == v and k in layer01_k:
                        if k == 1:
                            continue
                        elif k == 2:
                            self.other_states('W', 'G')
                            self.swap_adj_edges()
                            self.other_states('W', 'R', 'R')
                            break
                        elif k == 3:
                            self.other_states('W', 'O')
                            self.swap_adj_edges()
                            self.other_states('W', 'R', 'G')
                            break
                        elif k == 4:
                            self.other_states('W', 'O')
                            self.rotation_fi()
                            self.rotation_ui()
                            self.rotation_li()
                            self.rotation_u()
                            self.other_states('W', 'R', 'G')
                            break
                    elif e2 == v and k in layer01_k:
                        if k == 1:
                            self.other_states('W', 'G')
                            self.swap_adj_edges()
                            self.other_states('W', 'R', 'R')
                            break
                        elif k == 2:
                            continue
                        elif k == 3:
                            self.rotation_l()
                            self.rotation_u()
                            self.rotation_u()
                            self.rotation_li()
                            self.rotation_ui()
                            self.rotation_ui()
                            break
                        elif k == 4:
                            self.swap_adj_edges()
                            break
                    elif e3 == v and k in layer01_k:
                        if k == 1:
                            self.other_states('W', 'O')
                            self.swap_adj_edges()
                            self.other_states('W', 'R', 'G')
                            break
                        elif k == 2:
                            self.rotation_ri()
                            self.rotation_ui()
                            self.rotation_ui()
                            self.rotation_r()
                            self.rotation_u()
                            self.rotation_u()
                            break
                        elif k == 3:
                            continue
                        elif k == 4:
                            self.other_states('W', 'B')
                            self.swap_adj_edges()
                            self.other_states('W', 'R', 'O')
                            break
                    elif e4 == v and k in layer01_k:
                        if k == 1:
                            self.rotation_f()
                            self.rotation_u()
                            self.rotation_r()
                            self.rotation_ui()
                            break
                        elif k == 2:
                            self.swap_adj_edges()
                            break
                        elif k == 3:
                            self.other_states('W', 'B')
                            self.swap_adj_edges()
                            self.other_states('W', 'R', 'O')
                            break
                        elif k == 4:
                            continue
                    elif e5 == v and k in layer01_k:
                        if k == 1:
                            self.rotation_ui()
                            self.rotation_li()
                            self.rotation_u()
                            break
                        elif k == 2:
                            self.rotation_li()
                            break
                        elif k == 3:
                            self.rotation_u()
                            self.rotation_f()
                            self.rotation_ui()
                            break
                        elif k == 4:
                            self.rotation_f()
                            break
                    elif e6 == v and k in layer01_k:
                        if k == 1:
                            self.rotation_u()
                            self.rotation_r()
                            self.rotation_ui()
                            break
                        elif k == 2:
                            self.rotation_ui()
                            self.rotation_fi()
                            self.rotation_u()
                            break
                        elif k == 3:
                            self.rotation_r()
                            break
                        elif k == 4:
                            self.rotation_fi()
                            break
                    elif e7 == v and k in layer01_k:
                        if k == 1:
                            self.other_states('W', 'O')
                            self.rotation_fi()
                            self.other_states('W', 'R', 'G')
                            break
                        elif k == 2:
                            self.rotation_l()
                            break
                        elif k == 3:
                            self.rotation_u()
                            self.rotation_u()
                            self.rotation_l()
                            self.rotation_ui()
                            self.rotation_ui()
                            break
                        elif k == 4:
                            self.rotation_u()
                            self.rotation_l()
                            self.rotation_ui()
                            break
                    elif e8 == v and k in layer01_k:
                        if k == 1:
                            self.other_states('W', 'O')
                            self.rotation_f()
                            self.other_states('W', 'R', 'G')
                            break
                        elif k == 2:
                            self.rotation_ui()
                            self.rotation_ui()
                            self.rotation_ri()
                            self.rotation_u()
                            self.rotation_u()
                            break
                        elif k == 3:
                            self.rotation_ri()
                            break
                        elif k == 4:
                            self.rotation_ui()
                            self.rotation_ri()
                            self.rotation_u()
                            break
                    elif e9 == v and k in layer01_k:
                        if k == 1:
                            self.other_states('W', 'O')
                            self.rotation_di()
                            self.rotation_di()
                            self.rotation_fi()
                            self.rotation_fi()
                            self.other_states('W', 'R', 'G')
                            break
                        elif k == 2:
                            self.rotation_di()
                            self.rotation_li()
                            self.rotation_li()
                            self.rotation_li()
                            break
                        elif k == 3:
                            self.rotation_d()
                            self.rotation_r()
                            self.rotation_r()
                            break
                        elif k == 4:
                            self.rotation_f()
                            self.rotation_f()
                            break
                    elif e10 == v and k in layer01_k:
                        if k == 1:
                            self.other_states('W', 'O')
                            self.rotation_di()
                            self.rotation_fi()
                            self.rotation_fi()
                            self.other_states('W', 'R', 'G')
                            break
                        elif k == 2:
                            self.rotation_li()
                            self.rotation_li()
                            break
                        elif k == 3:
                            self.rotation_d()
                            self.rotation_d()
                            self.rotation_r()
                            self.rotation_r()
                            break
                        elif k == 4:
                            self.rotation_d()
                            self.rotation_f()
                            self.rotation_f()
                            break
                    elif e11 == v and k in layer01_k:
                        if k == 1:
                            self.other_states('W', 'O')
                            self.rotation_d()
                            self.rotation_f()
                            self.rotation_f()
                            self.other_states('W', 'R', 'G')
                            break
                        elif k == 2:
                            self.rotation_di()
                            self.rotation_di()
                            self.rotation_li()
                            self.rotation_li()
                            break
                        elif k == 3:
                            self.rotation_r()
                            self.rotation_r()
                            break
                        elif k == 4:
                            self.rotation_di()
                            self.rotation_f()
                            self.rotation_f()
                            break
                    elif e12 == v and k in layer01_k:
                        if k == 1:
                            self.other_states('W', 'O')
                            self.rotation_f()
                            self.rotation_f()
                            self.other_states('W', 'R', 'G')
                            break
                        elif k == 2:
                            self.rotation_d()
                            self.rotation_li()
                            self.rotation_li()
                            break
                        elif k == 3:
                            self.rotation_di()
                            self.rotation_r()
                            self.rotation_r()
                            break
                        elif k == 4:
                            self.rotation_di()
                            self.rotation_di()
                            self.rotation_f()
                            self.rotation_f()
                            break

                ep = self.get_edge_pc()
                e1, e2, e3, e4 = ep[1], ep[2], ep[3], ep[4]
                if e1 == edges[1] and e2 == edges[2] and e3 == edges[3] and e4 == edges[4]:
                    break
                else:
                    continue

        elif top == 'Y':
            # Work out every top edge piece of the yellow layer
            while True:
                ep = self.get_edge_pc()
                e1, e2, e3, e4 = ep[1], ep[2], ep[3], ep[4]
                for k, v in edges.items():
                    if e1 == v and k in layer01_k:
                        if k == 1:
                            continue
                        elif k == 2:
                            self.other_states('Y', 'B')
                            self.swap_adj_edges()
                            self.other_states('Y', 'R', 'R')
                            break
                        elif k == 3:
                            self.other_states('Y', 'O')
                            self.swap_adj_edges()
                            self.other_states('Y', 'R', 'B')
                            break
                        elif k == 4:
                            self.other_states('Y', 'O')
                            self.swap_adj_edges()
                            self.other_states('Y', 'R', 'B')
                            break
                    elif e2 == v and k in layer01_k:
                        if k == 1:
                            self.other_states('Y', 'B')
                            self.swap_adj_edges()
                            self.other_states('Y', 'R', 'R')
                            break
                        elif k == 2:
                            continue
                        elif k == 3:
                            self.other_states('Y', 'B')
                            self.swap_adj_edges()
                            self.other_states('Y', 'R', 'R')
                            break
                        elif k == 4:
                            self.swap_adj_edges()
                            break
                    elif e3 == v and k in layer01_k:
                        if k == 1:
                            self.other_states('Y', 'O')
                            self.swap_adj_edges()
                            self.other_states('Y', 'R', 'B')
                            break
                        elif k == 2:
                            self.other_states('Y', 'G')
                            self.swap_adj_edges()
                            self.other_states('Y', 'R', 'O')
                            break
                        elif k == 3:
                            continue
                        elif k == 4:
                            self.other_states('Y', 'G')
                            self.swap_adj_edges()
                            self.other_states('Y', 'R', 'O')
                            break
                    elif e4 == v and k in layer01_k:
                        if k == 1:
                            self.swap_adj_edges()
                            break
                        elif k == 2:
                            self.swap_adj_edges()
                            break
                        elif k == 3:
                            self.other_states('Y', 'G')
                            self.swap_adj_edges()
                            self.other_states('Y', 'R', 'O')
                            break
                        elif k == 4:
                            continue

                ep = self.get_edge_pc()
                e1, e2, e3, e4 = ep[1], ep[2], ep[3], ep[4]
                if e1 == edges[1] and e2 == edges[2] and e3 == edges[3] and e4 == edges[4]:
                    break
                else:
                    continue

    @log_function_call
    def corner_move(self, top, face, right, lay='not_last') -> None:
        """Rotate a corner piece to its right position.
        Algorithm R', D', R, D
        Executes at function corner_solving()"""
        if lay == 'not_last':
            while True:
                self.rotation_ri()
                self.rotation_di()
                self.rotation_r()
                self.rotation_d()

                if self.cube_up[8] == top and self.cube_face[2] == face and self.cube_right[0] == right:
                    self.other_states(top, 'R', right)
                    break
                else:
                    continue

        elif lay == 'last':
            while self.cube_up[8] != top:
                self.rotation_ri()
                self.rotation_di()
                self.rotation_r()
                self.rotation_d()

            self.other_states(top, 'R', right)

    @log_function_call
    def swap_adj_edges(self):
        """Swap adjacent edge pieces on the upper face to match them with their face color
        Two adjacent edge pieces are in correct position
        """
        # Algorithm R, U, Ri, U, R, U, U, Ri, U
        self.rotation_r()
        self.rotation_u()
        self.rotation_ri()

        self.rotation_u()
        self.rotation_r()
        self.rotation_u()

        self.rotation_u()
        self.rotation_ri()
        self.rotation_u()

    @log_function_call
    def arrange_upper_corners(self):
        """Moves corners in position 3, 1 in a clockwise way
        Corner 2 moves to 3 and 4 remains."""
        self.rotation_li()
        self.rotation_u()
        self.rotation_r()
        self.rotation_ui()
        self.rotation_l()
        self.rotation_u()
        self.rotation_ri()
        self.rotation_ui()

    @log_function_call
    def make_white_cross(self):
        """Create a white cross at the top face(white)."""
        # Bring white edges to their correct positions
        self.edge_solving(self.edge_pcs_white_up, 'W')
        # Ensure the white edges are well oriented
        while True:
            if self.cube_up[1] != 'W':
                self.other_states('W', 'O')
                self.edge_flip()
                self.other_states('W', 'R', 'G')
            elif self.cube_up[3] != 'W':
                self.other_states('W', 'G')
                self.edge_flip()
                self.other_states('W', 'R', 'R')
            elif self.cube_up[5] != 'W':
                self.other_states('W', 'B')
                self.edge_flip()
                self.other_states('W', 'R', 'O')
            elif self.cube_up[7] != 'W':
                self.edge_flip()

            if self.cube_up[1] == 'W' and self.cube_up[3] == 'W' and self.cube_up[5] == 'W' and self.cube_up[7] == 'W':
                break
            else:
                continue

    @log_function_call
    def edge_to_right_mid(self):
        """Swap edge piece on upper layer with one on middle layer.
        The middle layer edge piece is shared between the front and the right face."""
        self.rotation_u()
        self.rotation_r()
        self.rotation_ui()
        self.rotation_ri()
        self.rotation_ui()
        self.rotation_fi()
        self.rotation_u()
        self.rotation_f()

    @log_function_call
    def solve_mid_layer(self):
        """Solve the middle layer, matching all the colors."""
        while True:
            ep = self.get_edge_pc()
            if 'Y' not in ep[1]:
                to_swap = self.cube_back[1]
                if to_swap == 'G':
                    self.rotation_u()
                    if ep[1] == {'G', 'O'}:
                        self.other_states('Y', 'G')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'O')
                    elif ep[1] == {'G', 'R'}:
                        self.other_states('Y', 'G')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'O')
                elif to_swap == 'R':
                    self.rotation_u()
                    self.rotation_u()
                    if ep[1] == {'R', 'G'}:
                        self.edge_to_right_mid()
                    elif ep[1] == {'R', 'B'}:
                        self.edge_to_left_mid()
                elif to_swap == 'B':
                    self.rotation_ui()
                    if ep[1] == {'B', 'R'}:
                        self.other_states('Y', 'B')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'R')
                    elif ep[1] == {'B', 'O'}:
                        self.other_states('Y', 'B')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'R')
                elif to_swap == 'O':
                    if ep[1] == {'O', 'B'}:
                        self.other_states('Y', 'O')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'B')
                    elif ep[1] == {'O', 'G'}:
                        self.other_states('Y', 'O')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'B')
            elif 'Y' not in ep[2]:
                to_swap = self.cube_left[1]
                if to_swap == 'G':
                    self.rotation_ui()
                    self.rotation_ui()
                    if ep[2] == {'G', 'O'}:
                        self.other_states('Y', 'G')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'O')
                    elif ep[2] == {'G', 'R'}:
                        self.other_states('Y', 'G')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'O')
                elif to_swap == 'R':
                    self.rotation_ui()
                    if ep[2] == {'R', 'G'}:
                        self.edge_to_right_mid()
                    elif ep[2] == {'R', 'B'}:
                        self.edge_to_left_mid()
                elif to_swap == 'B':
                    if ep[2] == {'B', 'R'}:
                        self.other_states('Y', 'B')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'R')
                    elif ep[2] == {'B', 'O'}:
                        self.other_states('Y', 'B')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'R')
                elif to_swap == 'O':
                    self.rotation_u()
                    if ep[2] == {'O', 'B'}:
                        self.other_states('Y', 'O')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'B')
                    elif ep[2] == {'O', 'G'}:
                        self.other_states('Y', 'O')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'B')
            elif 'Y' not in ep[3]:
                to_swap = self.cube_right[1]
                if to_swap == 'G':
                    if ep[3] == {'G', 'O'}:
                        self.other_states('Y', 'G')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'O')
                    elif ep[3] == {'G', 'R'}:
                        self.other_states('Y', 'G')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'O')
                elif to_swap == 'R':
                    self.rotation_u()
                    if ep[3] == {'R', 'G'}:
                        self.edge_to_right_mid()
                    elif ep[3] == {'R', 'B'}:
                        self.edge_to_left_mid()
                elif to_swap == 'B':
                    self.rotation_u()
                    self.rotation_u()
                    if ep[3] == {'B', 'R'}:
                        self.other_states('Y', 'B')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'R')
                    elif ep[3] == {'B', 'O'}:
                        self.other_states('Y', 'B')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'R')
                elif to_swap == 'O':
                    self.rotation_ui()
                    if ep[3] == {'O', 'B'}:
                        self.other_states('Y', 'O')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'B')
                    elif ep[3] == {'O', 'G'}:
                        self.other_states('Y', 'O')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'B')
            elif 'Y' not in ep[4]:
                to_swap = self.cube_face[1]
                if to_swap == 'G':
                    self.rotation_ui()
                    if ep[4] == {'G', 'O'}:
                        self.other_states('Y', 'G')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'O')
                    elif ep[4] == {'G', 'R'}:
                        self.other_states('Y', 'G')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'O')
                elif to_swap == 'R':
                    if ep[4] == {'R', 'G'}:
                        self.edge_to_right_mid()
                    elif ep[4] == {'R', 'B'}:
                        self.edge_to_left_mid()
                elif to_swap == 'B':
                    self.rotation_u()
                    if ep[4] == {'B', 'R'}:
                        self.other_states('Y', 'B')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'R')
                    elif ep[4] == {'B', 'O'}:
                        self.other_states('Y', 'B')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'R')
                elif to_swap == 'O':
                    self.rotation_u()
                    self.rotation_u()
                    if ep[4] == {'O', 'B'}:
                        self.other_states('Y', 'O')
                        self.edge_to_right_mid()
                        self.other_states('Y', 'R', 'B')
                    elif ep[4] == {'O', 'G'}:
                        self.other_states('Y', 'O')
                        self.edge_to_left_mid()
                        self.other_states('Y', 'R', 'B')

            ep = self.get_edge_pc()
            edg_pcs = [self.edge_pcs_yellow_up[1], self.edge_pcs_yellow_up[2], self.edge_pcs_yellow_up[3],
                       self.edge_pcs_yellow_up[4]]
            if ep[1] in edg_pcs and ep[2] in edg_pcs and ep[3] in edg_pcs and ep[4] in edg_pcs:
                break
            else:
                continue

        if ((self.cube_face[3] == 'B' and self.cube_left[5] == 'R') or (self.cube_face[3] == 'R' and
                                                                        self.cube_left[5] == 'G')
                or (self.cube_face[3] == 'G' and self.cube_left[5] == 'R') or (self.cube_face[3] == 'G' and
                                                                               self.cube_left[5] == 'O')
                or (self.cube_face[3] == 'O' and self.cube_left[5] == 'G') or (self.cube_face[3] == 'B' and
                                                                               self.cube_left[5] == 'O')
                or (self.cube_face[3] == 'O' and self.cube_left[5] == 'B')):
            self.edge_to_left_mid()
            self.solve_mid_layer()

        elif ((self.cube_face[5] == 'G' and self.cube_right[3] == 'R') or (self.cube_face[5] == 'G' and
                                                                           self.cube_right[3] == 'O')
              or (self.cube_face[5] == 'O' and self.cube_right[3] == 'G') or (self.cube_face[5] == 'B' and
                                                                              self.cube_right[3] == 'R')
              or (self.cube_face[5] == 'R' and self.cube_right[3] == 'B') or (self.cube_face[5] == 'B' and
                                                                              self.cube_right[3] == 'O')
              or (self.cube_face[5] == 'O' and self.cube_right[3] == 'B')):
            self.edge_to_right_mid()
            self.solve_mid_layer()

        elif ((self.cube_left[3] == 'O' and self.cube_back[5] == 'B') or (self.cube_left[3] == 'G' and
                                                                          self.cube_back[5] == 'R')
              or (self.cube_left[3] == 'R' and self.cube_back[5] == 'G') or (self.cube_left[3] == 'O' and
                                                                             self.cube_back[5] == 'G')
              or (self.cube_left[3] == 'G' and self.cube_back[5] == 'O') or (self.cube_left[3] == 'R' and
                                                                             self.cube_back[5] == 'B')
              or (self.cube_left[3] == 'B' and self.cube_back[5] == 'R')):
            self.other_states('Y', 'B')
            self.edge_to_left_mid()
            self.other_states('Y', 'R', right='R')
            self.solve_mid_layer()

        elif ((self.cube_right[5] == 'O' and self.cube_back[3] == 'G') or (self.cube_right[5] == 'R' and
                                                                           self.cube_back[3] == 'B')
              or (self.cube_right[5] == 'B' and self.cube_back[3] == 'R') or (self.cube_right[5] == 'O' and
                                                                              self.cube_back[3] == 'B')
              or (self.cube_right[5] == 'B' and self.cube_back[3] == 'O') or (self.cube_right[5] == 'R' and
                                                                              self.cube_back[3] == 'G')
              or (self.cube_right[5] == 'G' and self.cube_back[3] == 'R')):
            self.other_states('Y', 'G')
            self.edge_to_right_mid()
            self.other_states('Y', 'R', right='O')
            self.solve_mid_layer()

    @log_function_call
    def edge_to_left_mid(self) -> None:
        """Swap edge piece on upper layer with one on middle layer.
        The middle layer edge piece is shared between the front face and the left face."""
        self.rotation_ui()
        self.rotation_li()
        self.rotation_u()
        self.rotation_l()
        self.rotation_u()
        self.rotation_f()
        self.rotation_ui()
        self.rotation_fi()

    @log_function_call
    def corner_solving(self) -> None:
        """Correctly solve the corner pieces.
        Does the necessary rotations to ensure the corners are well-placed therefore completing a layer(white)."""
        cp = self.get_corner_pc()
        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
        layer01_k = [1, 2, 3, 4]

        cOne, cTwo, cThree, cFour = ['W', 'G', 'O'], ['W', 'B', 'O'], ['W', 'G', 'R'], ['W', 'B', 'R']

        # Work out every corner piece of the white layer.
        while True:
            for k, v in self.corner_pcs_white_up.items():
                if c1 == v and k in layer01_k:
                    if k == 1 and [self.cube_up[0], self.cube_left[0], self.cube_back[2]] != cOne:
                        self.other_states('W', 'O')
                        self.corner_move('W', 'O', 'G')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 2 and [self.cube_up[2], self.cube_right[2], self.cube_back[0]] != cTwo:
                        self.other_states('W', 'B')
                        self.rotation_r()
                        self.rotation_di()
                        self.rotation_di()
                        self.rotation_ri()
                        self.rotation_d()
                        self.corner_move('W', 'B', 'O')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 3 and [self.cube_up[6], self.cube_left[2], self.cube_face[0]] != cThree:
                        self.other_states('W', 'G')
                        self.rotation_l()
                        self.rotation_d()
                        self.rotation_li()
                        self.corner_move('W', 'G', 'R')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 4 and [self.cube_up[8], self.cube_right[0], self.cube_face[2]] != cFour:
                        self.rotation_li()
                        self.rotation_d()
                        self.rotation_l()
                        self.rotation_d()
                        self.rotation_d()
                        self.corner_move('W', 'R', 'B')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                elif c2 == v and k in layer01_k:
                    if k == 1 and [self.cube_up[0], self.cube_left[0], self.cube_back[2]] != cOne:
                        self.rotation_r()
                        self.rotation_d()
                        self.rotation_ri()
                        self.other_states('W', 'O')
                        self.corner_move('W', 'O', 'G')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 2 and [self.cube_up[2], self.cube_right[2], self.cube_back[0]] != cTwo:
                        self.other_states('W', 'B')
                        self.corner_move('W', 'B', 'O')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 3 and [self.cube_up[6], self.cube_left[2], self.cube_face[0]] != cThree:
                        self.rotation_r()
                        self.rotation_di()
                        self.rotation_ri()
                        self.rotation_di()
                        self.rotation_di()
                        self.other_states('W', 'G')
                        self.corner_move('W', 'G', 'R')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 4 and [self.cube_up[8], self.cube_right[0], self.cube_face[2]] != cFour:
                        self.rotation_r()
                        self.rotation_di()
                        self.rotation_ri()
                        self.rotation_di()
                        self.corner_move('W', 'R', 'B')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                elif c3 == v and k in layer01_k:
                    if k == 1 and [self.cube_up[0], self.cube_left[0], self.cube_back[2]] != cOne:
                        self.rotation_l()
                        self.rotation_di()
                        self.rotation_li()
                        self.rotation_di()
                        self.other_states('W', 'O')
                        self.corner_move('W', 'O', 'G')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 2 and [self.cube_up[2], self.cube_right[2], self.cube_back[0]] != cTwo:
                        self.rotation_l()
                        self.rotation_d()
                        self.rotation_li()
                        self.rotation_d()
                        self.other_states('W', 'B')
                        self.corner_move('W', 'B', 'O')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 3 and [self.cube_up[6], self.cube_left[2], self.cube_face[0]] != cThree:
                        self.other_states('W', 'G')
                        self.corner_move('W', 'G', 'R')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 4 and [self.cube_up[8], self.cube_right[0], self.cube_face[2]] != cFour:
                        self.rotation_l()
                        self.rotation_d()
                        self.rotation_li()
                        self.corner_move('W', 'R', 'B')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                elif c4 == v and k in layer01_k:
                    if k == 1 and [self.cube_up[0], self.cube_left[0], self.cube_back[2]] != cOne:
                        self.rotation_ri()
                        self.rotation_di()
                        self.rotation_r()
                        self.rotation_di()
                        self.other_states('W', 'O')
                        self.corner_move('W', 'O', 'G')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 2 and [self.cube_up[2], self.cube_right[2], self.cube_back[0]] != cTwo:
                        self.rotation_ri()
                        self.rotation_d()
                        self.rotation_r()
                        self.rotation_d()
                        self.other_states('W', 'B')
                        self.corner_move('W', 'B', 'O')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 3 and [self.cube_up[6], self.cube_left[2], self.cube_face[0]] != cThree:
                        self.rotation_ri()
                        self.rotation_di()
                        self.rotation_r()
                        self.other_states('W', 'G')
                        self.corner_move('W', 'G', 'R')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 4 and [self.cube_up[8], self.cube_right[0], self.cube_face[2]] != cFour:
                        self.corner_move('W', 'R', 'B')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                elif c5 == v and k in layer01_k:
                    if k == 1 and [self.cube_up[0], self.cube_left[0], self.cube_back[2]] != cOne:
                        self.other_states('W', 'O')
                        self.corner_move('W', 'O', 'G')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 2 and [self.cube_up[2], self.cube_right[2], self.cube_back[0]] != cTwo:
                        self.rotation_di()
                        self.other_states('W', 'B')
                        self.corner_move('W', 'B', 'O')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 3 and [self.cube_up[6], self.cube_left[2], self.cube_face[0]] != cThree:
                        self.rotation_d()
                        self.other_states('W', 'G')
                        self.corner_move('W', 'G', 'R')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 4 and [self.cube_up[8], self.cube_right[0], self.cube_face[2]] != cFour:
                        self.rotation_d()
                        self.rotation_d()
                        self.corner_move('W', 'R', 'B')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                elif c6 == v and k in layer01_k:
                    if k == 1 and [self.cube_up[0], self.cube_left[0], self.cube_back[2]] != cOne:
                        self.rotation_d()
                        self.other_states('W', 'O')
                        self.corner_move('W', 'O', 'G')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 2 and [self.cube_up[2], self.cube_right[2], self.cube_back[0]] != cTwo:
                        self.other_states('W', 'B')
                        self.corner_move('W', 'B', 'O')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 3 and [self.cube_up[6], self.cube_left[2], self.cube_face[0]] != cThree:
                        self.rotation_di()
                        self.rotation_di()
                        self.other_states('W', 'G')
                        self.corner_move('W', 'G', 'R')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 4 and [self.cube_up[8], self.cube_right[0], self.cube_face[2]] != cFour:
                        self.rotation_di()
                        self.corner_move('W', 'R', 'B')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                elif c7 == v and k in layer01_k:
                    if k == 1 and [self.cube_up[0], self.cube_left[0], self.cube_back[2]] != cOne:
                        self.rotation_di()
                        self.other_states('W', 'O')
                        self.corner_move('W', 'O', 'G')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 2 and [self.cube_up[2], self.cube_right[2], self.cube_back[0]] != cTwo:
                        self.rotation_d()
                        self.rotation_d()
                        self.other_states('W', 'B')
                        self.corner_move('W', 'B', 'O')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 3 and [self.cube_up[6], self.cube_left[2], self.cube_face[0]] != cThree:
                        self.other_states('W', 'G')
                        self.corner_move('W', 'G', 'R')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 4 and [self.cube_up[8], self.cube_right[0], self.cube_face[2]] != cFour:
                        self.rotation_d()
                        self.corner_move('W', 'R', 'B')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                elif c8 == v and k in layer01_k:
                    if k == 1 and [self.cube_up[0], self.cube_left[0], self.cube_back[2]] != cOne:
                        self.rotation_di()
                        self.rotation_di()
                        self.other_states('W', 'O')
                        self.corner_move('W', 'O', 'G')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 2 and [self.cube_up[2], self.cube_right[2], self.cube_back[0]] != cTwo:
                        self.rotation_d()
                        self.other_states('W', 'B')
                        self.corner_move('W', 'B', 'O')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 3 and [self.cube_up[6], self.cube_left[2], self.cube_face[0]] != cThree:
                        self.rotation_di()
                        self.other_states('W', 'G')
                        self.corner_move('W', 'G', 'R')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break
                    elif k == 4 and [self.cube_up[8], self.cube_right[0], self.cube_face[2]] != cFour:
                        self.corner_move('W', 'R', 'B')
                        cp = self.get_corner_pc()
                        c1, c2, c3, c4, c5, c6, c7, c8 = cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7], cp[8]
                        break

            if self.cube_face[4] == 'G':
                self.other_states('W', 'R', 'R')
            elif self.cube_face[4] == 'B':
                self.other_states('W', 'R', 'O')
            elif self.cube_face[4] == 'O':
                self.other_states('W', 'R', 'G')

            if (self.cube_up[0] == self.cube_up[2] == self.cube_up[6] == self.cube_up[8] == 'W' and
                    self.cube_left[0] == self.cube_left[2] == 'G' and self.cube_face[0] == self.cube_face[2] == 'R'
                    and self.cube_right[0] == self.cube_right[2] == 'B' and
                    self.cube_back[0] == self.cube_back[2] == 'O'):
                break
            else:
                continue

    @staticmethod
    @log_function_call
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
                print("Please type 1 to proceed.")
                trials += 1
                continue

    @staticmethod
    @log_function_call
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

    @log_function_call
    def results(self):
        """Shows the steps to solve the cube."""

        step = 1
        moves = [i for i in self.solution if type(i) is str]

        start_stat = f"\nYou'll be able to solve the cube in {len(moves)} steps if you follow the steps keenly.\n"
        print(start_stat.center(len(start_stat) + 10), '-')
        for n in range(len(self.solution)):
            if self.solution[n] == ['<<< ALL DONE🎉>>>']:
                print(f"\n{self.solution[-1][0]}\n")
                break
            elif (self.solution[n] != ['<<< ALL DONE🎉>>>'] and type(self.solution[n]) is list and
                  type(self.solution[n + 1]) is list):
                del self.solution[n]
                if type(self.solution[n + 1]) is list:
                    continue
                else:
                    if self.proceed():
                        print(f"\n<<<{self.solution[n][0]}>>> \n")
            elif (self.solution[n] != ['<<< ALL DONE🎉>>>'] and type(self.solution[n]) is list and
                  type(self.solution[n + 1]) is not list):
                if self.proceed():
                    print(f'\n<<<{self.solution[n][0]}>>> \n')
            else:
                if self.proceed():
                    print(f"\nStep {step} <<<{self.symbol_meaning(self.solution[n])}>>>")
                    step += 1

    @log_function_call
    def color_entry(self):
        """Receives and validates user input."""
        print('COLOR ENTRY INSTRUCTIONS\n\n'
              '1. Start face color entry with the red center piece on the front face and '
              'white center piece in the top face'
              '\n2. Enter the yellow face while the red center piece is on the top face. \n'
              '3. Enter the colors starting from the top left corner of each face and '
              'end at the bottom right corner-\n')

        face_len = 1
        attempts = 0
        faces = []
        # while face_len <= 6:
        while face_len > 6:
            if attempts == 6:
                sys.exit('Please ensure you enter the correct colors as indicated in the instructions.')
            face_input = list(input(f'Face {face_len}: ').upper().strip())
            if len(face_input) == 9:
                faces.append(face_input)
                if self.number_color_check(faces) is False:
                    faces.pop(-1)
                    print(f'\nPlease enter valid Rubik\'s cube colors. {attempts} attempts remaining.\n')
                    attempts += 1
                else:
                    face_len += 1
            else:
                print(f'\nA face has 9 colors. {attempts} attempts left.\n')
                attempts += 1

        faces = [list('oywbwyywy'.upper()), list('grbwrbbog'.upper()), list('rrryboyog'.upper()),
                 list('ogogybgyw'.upper()), list('bowwogogw'.upper()), list('brrrgbrwy'.upper())]

        return faces

    @log_function_call
    def number_color_check(self, face_colors):
        """Check whether all colors are entered and are valid."""
        colors_list = [c for c_lis in face_colors for c in c_lis]

        # Check for invalid colors
        for s in colors_list:
            if s not in self.valid_colors.keys():
                print(f"Invalid color '{s}' entered. Re-enter the face colors.\n")
                return False
            if colors_list.count(s) > 9:
                sys.exit(f'{self.valid_colors[s]} tiles exceeds 9')

        return True

    @log_function_call
    def color_map(self):
        """Identify face color and orient as needed.
           Default orientation when Yellow and White are up or down"""
        face_colors = self.color_entry()
        for c in face_colors:
            if c[4] == 'W':
                self.cube_up = c
            elif c[4] == 'R':
                self.cube_face = c
            elif c[4] == 'G':
                self.cube_left = c
            elif c[4] == 'B':
                self.cube_right = c
            elif c[4] == 'Y':
                self.cube_down = c
            elif c[4] == 'O':
                self.cube_back = c
