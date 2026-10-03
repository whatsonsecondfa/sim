image head = "owl head.png"

image head = "owl head.png"
image cheeks = "cheeks.png"
image neck = "neck.png"
image torso = "owl body.png"
image boob_left = "owl boob left.png"
image boob_left_top = "owl boob left top.png"
image boob_left_bottom = "owl boob left bottom.png"
image boob_right = "owl boob right.png"
image boob_right_top = "owl boob right top.png"
image boob_right_bottom = "owl boob right bottom.png"
image stomach = "owl stomach.png"
image stomach_top = "owl stomach top.png"
image stomach_bottom = "owl stomach bottom.png"
image arm_left = "owl arm left.png"
image arm_right = "owl arm right.png"
image leg_left = "owl leg left.png"
image leg_right = "owl leg right.png"

define owl_center = 1920 / 2

#standard scale
define s = 0.47

#temp scale for when showing bounces
define tsx = 0.47
define tsy = 0.47

#bounce phases 1, 2, 3
define b1 = 0.125
define b2 = 0.025
define b3 = 0.0125

#total bounce time
define bt = 1.5

#boob init
define b_width_growth = 25
define btl_x = 800
define bt_y = 500
define bt_width = 100 * s
define bt_height = 252 * s
define bbl_x = btl_x
define bb_y = bt_y + bt_height
define bb_width = 307 * s
define bb_height = 159 * s
define bbr_x = 975
define btr_x = bbr_x + bb_width - bt_width

define s_width = 1
define s_height = 1
define st_width = 481 * s
define st_height = 131 * s
define st_width_growth = 25
define st_height_growth = 10
define st_x = 848
define st_y = 683
define st_x_move = -8
define st_y_move = -15
define st_a = 0

define sb_width = 478 * s
define sb_height = 363 * s
define sb_width_growth = 25
define sb_height_growth = 10
define sb_x = 845
define sb_y = 740
define sb_a = 0
define sb_x_move = -8
define sb_y_move = 0

define ll_width = 531 * s
define ll_height = 494 * s
define ll_x = 715
define ll_y = 850
define lr_width = 531 * s
define lr_height = 494 * s
define lr_x = 950
define lr_y = 850
define l_width_growth = 25

init python:
    class Part:
        def __init__(self, sprite, anchor, x, y, width, height):
            self.anchor = anchor
            self.sprite = sprite
            self.x = x
            self.y = y
            self.width = width
            self.height = height

label showFeedee:

    $ head = Part("head", "left", -5, 55, 1920, 1080)
    show expression "%s" % head.sprite at showPart(0, 1, head.x, head.y, head.width, head.height)

    $ left_arm = Part("arm_left", "left", -5, 40, 1920, 1080)
    show expression "%s" % left_arm.sprite at showPart(0, 1, left_arm.x, left_arm.y, left_arm.width, left_arm.height)

    $ right_arm = Part("arm_right", "left", -5, 40, 1920, 1080)
    show expression "%s" % right_arm.sprite at showPart(0, 1, right_arm.x, right_arm.y, right_arm.width, right_arm.height)

    #show arm_left at owlArmLeft
    #show arm_right at owlArmRight
    show torso at owlBody
    show leg_left at owlLegLeft
    show leg_right at owlLegRight
    show stomach_top at owlStomachTop
    show stomach_bottom at owlStomachBottom

    $ btl = Part("boob_left_top", "left", btl_x, bt_y, bt_width, bt_height)
    show expression "%s" % btl.sprite at showPart(0, 1, btl.x, btl.y, btl.width, btl.height)

    $ bbl = Part("boob_left_bottom", "left", bbl_x, bb_y, bb_width, bb_height)
    show expression "%s" % bbl.sprite at showPart(0, 1, bbl.x, bbl.y, bbl.width, bbl.height)

    $ btr = Part("boob_right_top", "left", btr_x, bt_y, bt_width, bt_height)
    show expression "%s" % btr.sprite at showPart(0, 1, btr.x, btr.y, btr.width, btr.height)

    $ bbr = Part("boob_right_bottom", "left", bbr_x, bb_y, bb_width, bb_height)
    show expression "%s" % bbr.sprite at showPart(0, 1, bbr.x, bbr.y, bbr.width, bbr.height)

    jump interaction

    return

transform fatten(x_pos, x_size, y_pos, y_size, new_alpha):
    linear bt xysize(int(x_size), int(y_size)) pos(int(x_pos), int(y_pos)) alpha new_alpha

label interaction:

    $ tsx = s
    $ tsy = s

    menu:

        "What do?"

        "Bounce boobs":

            window hide

            $ time = 1 * bt / 20

            $ top_height_1 = bt_height / (1 + b1)
            $ width_diff_1 = bt_width * (1 + b1)

            show expression "%s" % btl.sprite at showPart(time, 1, btl.x - width_diff_1, btl.y, btl.width + width_diff_1, top_height_1)
            show expression "%s" % bbl.sprite at showPart(time, 1, bbl.x - width_diff_1, btl.y + top_height_1, bbl.width + width_diff_1, bbl.height / (1 + b1))

            show expression "%s" % btr.sprite at showPart(time, 1, btr.x, btr.y, btr.width + width_diff_1, top_height_1)
            show expression "%s" % bbr.sprite at showPart(time, 1, bbr.x, btr.y + top_height_1, bbr.width + width_diff_1, bbr.height / (1 + b1))

            pause (time)

            $ time = 3 * bt / 20

            $ top_height_2 = (bt_height / (1 - b1))
            $ width_diff_2 = (bt_width * (1 + b1)) / 20

            show expression "%s" % btl.sprite at showPart(time, 1, btl.x - width_diff_2, btl.y, btl.width + width_diff_2, top_height_2)
            show expression "%s" % bbl.sprite at showPart(time, 1, bbl.x - width_diff_2, btl.y + top_height_2, bbl.width + width_diff_2, bbl.height / (1 + b1))

            show expression "%s" % btr.sprite at showPart(time, 1, btr.x, btr.y, btr.width + width_diff_2, top_height_2)
            show expression "%s" % bbr.sprite at showPart(time, 1, bbr.x, btr.y + top_height_2, bbr.width + width_diff_2, bbr.height / (1 + b2))

            pause (time)

            $ top_height_3 = (bt_height / (1 + b2))
            $ width_diff_3 = bt_width * (1 + b2)

            show expression "%s" % btl.sprite at showPart(time, 1, btl.x - width_diff_3, btl.y, btl.width + width_diff_3, top_height_3)
            show expression "%s" % bbl.sprite at showPart(time, 1, bbl.x - width_diff_3, btr.y + top_height_3, bbl.width + width_diff_3, bbl.height / (1 + b3))

            show expression "%s" % btr.sprite at showPart(time, 1, btr.x, btr.y, btr.width + width_diff_3, top_height_3)
            show expression "%s" % bbr.sprite at showPart(time, 1, bbr.x, btr.y + top_height_3, bbr.width + width_diff_3, bbr.height / (1 + b3))

            pause (time)

            $ time = bt / 5

            show expression "%s" % btl.sprite at showPart(time, 1, btl.x, btl.y, btl.width, btl.height)
            show expression "%s" % bbl.sprite at showPart(time, 1, bbl.x, bbl.y, bbl.width, bbl.height)

            show expression "%s" % btr.sprite at showPart(time, 1, btr.x, btr.y, btr.width, btr.height)
            show expression "%s" % bbr.sprite at showPart(time, 1, bbr.x, bbr.y, bbr.width, bbr.height)

            pause (time)

        "Bounce belly":

            window hide
            show stomach_top at bounceStomachTop
            show stomach_bottom at bounceStomachBottom
            pause bt

        "Bounce legs":

            window hide
            show leg_left at bounceLegLeft
            show leg_right at bounceLegRight
            pause bt

        "Fatten boobs":

            call fatten("boobs")

        "Fatten belly":

            call fatten("stomach")

        "Fatten legs":

            call fatten("legs")

    jump interaction

#    pause

label fatten(part):
    window hide
    if part == "boobs":

        $ time = bt

        $ btl.width += b_width_growth
        $ btl.x -= b_width_growth
        show expression "%s" % btl.sprite at showPart(time, 1, btl.x, btl.y, btl.width, btl.height)

        $ bbl.width += b_width_growth
        $ bbl.x -= b_width_growth
        show expression "%s" % bbl.sprite at showPart(time, 1, bbl.x, bbl.y, bbl.width, bbl.height)

        $ btr.width += b_width_growth
        show expression "%s" % btr.sprite at showPart(time, 1, btr.x, btr.y, btr.width, btr.height)

        $ bbr.width += b_width_growth
        show expression "%s" % bbr.sprite at showPart(time, 1, bbr.x, bbr.y, bbr.width, bbr.height)

        pause time

    elif part == "stomach":

        $ sb_width += sb_width_growth
        $ sb_height += sb_height_growth
        $ sb_x = owl_center - (sb_width / 2)
        $ sb_y += sb_y_move
        $ sb_a = 1

        show stomach_bottom at fatten(sb_x, sb_width, sb_y, sb_height, sb_a)

        $ st_width += st_width_growth
        $ st_height += st_height_growth
        $ st_x = (owl_center + 3) - (st_width / 2)
        $ st_y = sb_y - st_height + 2

        if st_width > 300:
            $ st_a = 1

        show stomach_top at fatten(st_x, st_width, st_y, st_height, st_a)

        pause bt

    elif part == "legs":

        $ ll_width += l_width_growth
        $ ll_x -= l_width_growth
        $ lr_width += l_width_growth

        show leg_left at fatten(ll_x, ll_width, ll_y, ll_height, 1)
        show leg_right at fatten(lr_x, lr_width, lr_y, lr_height, 1)

        pause bt

transform owlHead:
    xzoom tsx yzoom tsy center

transform owlBody:
    xzoom tsx yzoom tsy center

transform owlArmLeft:
    xzoom tsx yzoom tsy center

transform owlArmRight:
    xzoom tsx yzoom tsy center

transform owlLegLeft:
    #xzoom tsx yzoom tsy center
    xysize(int(ll_width), int(ll_height))
    pos(int(ll_x), int(ll_y))

transform owlLegRight:
    #xzoom tsx yzoom tsy center
    xysize(int(lr_width), int(lr_height))
    pos(int(lr_x), int(lr_y))

transform owlStomachTop:
    xysize(int(st_width), int(st_height))
    pos(int(st_x), int(st_y))
    alpha st_a

transform owlStomachBottom:
    xysize(int(sb_width), int(sb_height))
    pos(int(sb_x), int(sb_y))
    alpha sb_a

transform bounceStomachTop:

    linear (1 * bt / 20) xysize(int(st_width * (1 + b1)), int(st_height / (1 + b1))) pos(3 + int(owl_center - (st_width * (1 + b1)) / 2), int(3 + sb_y - st_height / (1 + b1)))

    linear (3 * bt / 20) xysize(int(st_width * (1 - b1)), int(st_height / (1 - b1))) pos(3 + int(owl_center - (st_width * (1 - b1)) / 2), int(3 + sb_y - st_height / (1 - b1)))

    linear (3 * bt / 20) xysize(int(st_width * (1 + b2)), int(st_height / (1 + b2))) pos(3 + int(owl_center - (st_width * (1 + b2)) / 2), int(3 + sb_y - st_height / (1 + b2)))

    linear (bt / 5) xysize(int(globals()['st_width']), int(globals()['st_height'])) pos(int(st_x), int(st_y))

transform bounceStomachBottom:

    linear (1 * bt / 20):
        xysize(int(sb_width * (1 + b1)), int(sb_height / (1 + b1)))
        pos(int(owl_center - (sb_width * (1 + b1)) / 2), int(sb_y))

    linear (3 * bt / 20):
        xysize(int(sb_width * (1 - b1)), int(sb_height / (1 - b1)))
        pos(int(owl_center - (sb_width * (1 - b1)) / 2), int(sb_y))

    linear (3 * bt / 20):
        xysize(int(sb_width * (1 + b2)), int(sb_height / (1 + b2)))
        pos(int(owl_center - (sb_width * (1 + b2)) / 2), int(sb_y))

    linear (bt / 5):
        xysize(int(globals()['sb_width']), int(globals()['sb_height']))
        pos(int(sb_x), int(sb_y))

transform bounceLegLeft:

    linear (1 * bt / 20):
        xysize(int(ll_width * (1 + b1)), int(ll_height / (1 + b1)))
        pos(int(ll_x + ll_width - (ll_width * (1 + b1))), int(ll_y + ll_height - (ll_height / (1 + b1))))

    linear (3 * bt / 20):
        xysize(int(ll_width * (1 - b1)), int(ll_height / (1 - b1)))
        pos(int(ll_x + ll_width - (ll_width * (1 - b1))), int(ll_y + ll_height - (ll_height / (1 - b1))))

    linear (3 * bt / 20):
        xysize(int(ll_width * (1 + b2)), int(ll_height / (1 + b2)))
        pos(int(ll_x + ll_width - (ll_width * (1 + b2))), int(ll_y + ll_height - (ll_height / (1 + b2))))

    linear (bt / 5):
        xysize(int(globals()['ll_width']), int(globals()['ll_height']))
        pos(int(ll_x), int(ll_y))

transform bounceLegRight:

    linear (1 * bt / 20):
        xysize(int(lr_width * (1 + b1)), int(lr_height / (1 + b1)))
        pos(int(lr_x), int(lr_y + lr_height - (lr_height / (1 + b1))))

    linear (3 * bt / 20):
        xysize(int(lr_width * (1 - b1)), int(lr_height / (1 - b1)))
        pos(int(lr_x), int(lr_y + lr_height - (lr_height / (1 - b1))))

    linear (3 * bt / 20):
        xysize(int(lr_width * (1 + b2)), int(lr_height / (1 + b2)))
        pos(int(lr_x), int(lr_y + lr_height - (lr_height / (1 + b2))))

    linear (bt / 5):
        xysize(int(globals()['lr_width']), int(globals()['lr_height']))
        pos(int(lr_x), int(lr_y))

transform showPart(time, new_alpha, x, y, width, height):
    linear (time):
        xysize(int(width), int(height))
        pos(int(x), int(y))
        alpha new_alpha
