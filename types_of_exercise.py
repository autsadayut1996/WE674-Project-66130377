import numpy as np
from body_part_angle import BodyPartAngle
from utils import *


class TypeOfExercise(BodyPartAngle):
    def __init__(self, landmarks):
        super().__init__(landmarks)

    def push_up(self, counter, status):
        left_arm_angle = self.angle_of_the_left_arm()
        right_arm_angle = self.angle_of_the_left_arm()
        avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

        if status:
            if avg_arm_angle < 70:
                counter += 1
                status = False
        else:
            if avg_arm_angle > 160:
                status = True

        return [counter, status]   

    def pull_up(self, counter, status):
        nose = detection_body_part(self.landmarks, "NOSE")
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        avg_shoulder_y = (left_elbow[1] + right_elbow[1]) / 2

        if status:
            if nose[1] > avg_shoulder_y:
                counter += 1
                status = False

        else:
            if nose[1] < avg_shoulder_y:
                status = True

        return [counter, status]

    def squat(self, counter, status):
        left_leg_angle = self.angle_of_the_right_leg()
        right_leg_angle = self.angle_of_the_left_leg()
        avg_leg_angle = (left_leg_angle + right_leg_angle) // 2

        if status:
            if avg_leg_angle < 70:
                counter += 1
                status = False
        else:
            if avg_leg_angle > 160:
                status = True

        return [counter, status]

    def walk(self, counter, status):
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")

        if status:
            if left_knee[0] > right_knee[0]:
                counter += 1
                status = False

        else:
            if left_knee[0] < right_knee[0]:
                counter += 1
                status = True

        return [counter, status]

    def sit_up(self, counter, status):
        angle = self.angle_of_the_abdomen()
        if status:
            if angle < 55:
                counter += 1
                status = False
        else:
            if angle > 105:
                status = True

        return [counter, status]
    
    def army_crawl(self, counter, status):
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")

        if status:
            if left_elbow[1] > left_knee[1] and right_elbow[1] > right_knee[1]:
                counter += 1
                status = False
        else:
            if left_elbow[1] < left_knee[1] and right_elbow[1] < right_knee[1]:
                status = True

        return [counter, status]
    
    def bounces(self, counter, status):
        left_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_ankle = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2

        if status:
            if left_ankle[1] > hip_center and right_ankle[1] > hip_center:
                counter += 1
                status = False
        else:
            if left_ankle[1] < hip_center and right_ankle[1] < hip_center:
                status = True

        return [counter, status]
    
    def crunches(self, counter, status):
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        right_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2

    
        if status:
            if left_shoulder[1] > hip_center and right_shoulder[1] > hip_center:
                counter += 1
                status = False
        else:
            if left_shoulder[1] < hip_center and right_shoulder[1] < hip_center:
                status = True
        return [counter, status]
    
    def l_sit_ups(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if left_knee[1] < hip_center and right_knee[1] < hip_center:
                counter += 1
                status = False
        else:
            if left_knee[1] > hip_center and right_knee[1] > hip_center:
                status = True
        return [counter, status]
    
    def pop_up_tripod(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        if status:
            if left_hand[1] < left_knee[1] and right_hand[1] < right_knee[1]:
                counter += 1
                status = False
        else:
            if left_hand[1] > left_knee[1] and right_hand[1] > right_knee[1]:
                status = True
        return [counter, status]
    
    def raised_leg_crunches(self, counter, status):
        left_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_ankle = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if left_ankle[1] < hip_center and right_ankle[1] < hip_center:
                counter += 1
                status = False
        else:
            if left_ankle[1] > hip_center and right_ankle[1] > hip_center:
                status = True
        return [counter, status]
    
    def scissors(self, counter, status):
        left_leg = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_leg = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        if status:
            if left_leg[0] < right_leg[0]:
                counter += 1
                status = False
        else:
            if left_leg[0] > right_leg[0]:
                status = True
        return [counter, status]
    
    def sit_up_elbow_strikes(self, counter, status):
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        if status:
            if abs(left_elbow[0] - left_knee[0]) < 0.1 or abs(right_elbow[0] - right_knee[0]) < 0.1:
                counter += 1
                status = False
        else:
            if abs(left_elbow[0] - left_knee[0]) > 0.2 and abs(right_elbow[0] - right_knee[0]) > 0.2:
                status = True
        return [counter, status]
    
    def sitting_punches(self, counter, status):
        left_wrist = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_wrist = detection_body_part(self.landmarks, "RIGHT_WRIST")

        if status:
            if left_wrist[0] > 0.6 or right_wrist[0] > 0.6:
                counter += 1
                status = False
        else:
            if left_wrist[0] < 0.4 and right_wrist[0] < 0.4:
                status = True
        return [counter, status]
    
    def superman(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        left_foot = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_foot = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        if status:
            if left_hand[1] < left_foot[1] and right_hand[1] < right_foot[1]:
                counter += 1
                status = False
        else:
            if left_hand[1] > left_foot[1] and right_hand[1] > right_foot[1]:
                status = True
        return [counter, status]
    
    def thigh_taps(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        left_thigh = detection_body_part(self.landmarks, "LEFT_HIP")
        right_thigh = detection_body_part(self.landmarks, "RIGHT_HIP")
        if status:
            if abs(left_hand[1] - left_thigh[1]) < 0.1 or abs(right_hand[1] - right_thigh[1]) < 0.1:
                counter += 1
                status = False
        else:
            if abs(left_hand[1] - left_thigh[1]) > 0.2 and abs(right_hand[1] - right_thigh[1]) > 0.2:
                status = True
        return [counter, status]

    def accordion_push_ups(self, counter, status):
        chest = detection_body_part(self.landmarks, "NOSE")
        hands = [
            detection_body_part(self.landmarks, "LEFT_WRIST"),
            detection_body_part(self.landmarks, "RIGHT_WRIST"),
        ]
        if status:
            if chest[1] < hands[0][1] and chest[1] < hands[1][1]:
                counter += 1
                status = False
        else:
            if chest[1] > hands[0][1] and chest[1] > hands[1][1]:
                status = True
        return [counter, status]

    def air_bike_crunches(self, counter, status):
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        if status:
            if abs(left_elbow[0] - right_knee[0]) < 0.1 or abs(right_elbow[0] - left_knee[0]) < 0.1:
                counter += 1
                status = False
        else:
            if abs(left_elbow[0] - right_knee[0]) > 0.2 and abs(right_elbow[0] - left_knee[0]) > 0.2:
                status = True
        return [counter, status]

    def balance_side_lunges(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_ankle = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        if status:
            if left_knee[0] < left_ankle[0] or right_knee[0] > right_ankle[0]:
                counter += 1
                status = False
        else:
            if left_knee[0] > left_ankle[0] and right_knee[0] < right_ankle[0]:
                status = True
        return [counter, status]

    def bear_crawl(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        if status:
            if left_hand[1] > left_knee[1] and right_hand[1] > right_knee[1]:
                counter += 1
                status = False
        else:
            if left_hand[1] < left_knee[1] and right_hand[1] < right_knee[1]:
                status = True
        return [counter, status]

    def body_saw(self, counter, status):
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        shoulder_center = (self.landmarks["LEFT_SHOULDER"][1] + self.landmarks["RIGHT_SHOULDER"][1]) / 2
        if status:
            if shoulder_center > hip_center:
                counter += 1
                status = False
        else:
            if shoulder_center < hip_center:
                status = True
        return [counter, status]

    def burpees_with_push_up(self, counter, status):
        chest = detection_body_part(self.landmarks, "NOSE")
        feet = [
            detection_body_part(self.landmarks, "LEFT_ANKLE"),
            detection_body_part(self.landmarks, "RIGHT_ANKLE"),
    ]
        if status:
            if chest[1] < feet[0][1] and chest[1] < feet[1][1]:
                counter += 1
                status = False
        else:
            if chest[1] > feet[0][1] and chest[1] > feet[1][1]:
                status = True
        return [counter, status]

    def burpees_with_rotations(self, counter, status):
        shoulder_center = (self.landmarks["LEFT_SHOULDER"][0] + self.landmarks["RIGHT_SHOULDER"][0]) / 2
        hip_center = (self.landmarks["LEFT_HIP"][0] + self.landmarks["RIGHT_HIP"][0]) / 2
        if status:
            if abs(shoulder_center - hip_center) > 0.2:
                counter += 1
                status = False
        else:
            if abs(shoulder_center - hip_center) < 0.1:
                status = True
        return [counter, status]

    def burpees(self, counter, status):
        chest = detection_body_part(self.landmarks, "NOSE")
        feet = [
            detection_body_part(self.landmarks, "LEFT_ANKLE"),
            detection_body_part(self.landmarks, "RIGHT_ANKLE"),
    ]
        if status:
            if chest[1] > feet[0][1] and chest[1] > feet[1][1]:
                counter += 1
                status = False
        else:
            if chest[1] < feet[0][1] and chest[1] < feet[1][1]:
                status = True
        return [counter, status]

    def butt_kicks(self, counter, status):
        left_heel = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_heel = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if abs(left_heel[1] - hip_center) < 0.1 or abs(right_heel[1] - hip_center) < 0.1:
                counter += 1
                status = False
        else:
            if abs(left_heel[1] - hip_center) > 0.2 and abs(right_heel[1] - hip_center) > 0.2:
                status = True
        return [counter, status]

    def calf_raises(self, counter, status):
        left_heel = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_heel = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        ground_level = 0.1 
        if status:
            if left_heel[1] > ground_level and right_heel[1] > ground_level:
                counter += 1
                status = False
        else:
            if left_heel[1] <= ground_level and right_heel[1] <= ground_level:
                status = True
        return [counter, status]

    def chest_expansions(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        chest = detection_body_part(self.landmarks, "NOSE")
        if status:
            if abs(left_hand[0] - chest[0]) > 0.5 and abs(right_hand[0] - chest[0]) > 0.5:
                counter += 1
                status = False
        else:
            if abs(left_hand[0] - chest[0]) < 0.3 and abs(right_hand[0] - chest[0]) < 0.3:
                status = True
        return [counter, status]

    def climber_taps(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        hands = [
            detection_body_part(self.landmarks, "LEFT_WRIST"),
            detection_body_part(self.landmarks, "RIGHT_WRIST"),
    ]
        if status:
            if abs(left_knee[1] - hands[0][1]) < 0.1 or abs(right_knee[1] - hands[1][1]) < 0.1:
                counter += 1
                status = False
        else:
            if abs(left_knee[1] - hands[0][1]) > 0.2 and abs(right_knee[1] - hands[1][1]) > 0.2:
                status = True
        return [counter, status]

    def climbers(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if left_knee[1] < hip_center or right_knee[1] < hip_center:
                counter += 1
                status = False
        else:
            if left_knee[1] > hip_center and right_knee[1] > hip_center:
                status = True
        return [counter, status]

    def close_grip(self, counter, status):
        hands_distance = abs(
            detection_body_part(self.landmarks, "LEFT_WRIST")[0] -
            detection_body_part(self.landmarks, "RIGHT_WRIST")[0]
    )
        if status:
            if hands_distance < 0.2:
                counter += 1
                status = False
        else:
            if hands_distance > 0.3:
                status = True
        return [counter, status]

    def curtsy_lunges(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_ankle = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        if status:
            if left_knee[0] < right_ankle[0] or right_knee[0] > left_ankle[0]:
                counter += 1
                status = False
        else:
            if left_knee[0] > left_ankle[0] and right_knee[0] < right_ankle[0]:
                status = True
        return [counter, status]

    def dragon_push_ups(self, counter, status):
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        chest = detection_body_part(self.landmarks, "NOSE")
        if status:
            if chest[1] < left_elbow[1] and chest[1] < right_elbow[1]:
                counter += 1
                status = False
        else:
            if chest[1] > left_elbow[1] and chest[1] > right_elbow[1]:
                status = True
        return [counter, status]

    def dynamic_squats(self, counter, status):
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        knee_center = (self.landmarks["LEFT_KNEE"][1] + self.landmarks["RIGHT_KNEE"][1]) / 2
        if status:
            if hip_center > knee_center:
                counter += 1
                status = False
        else:
            if hip_center <= knee_center:
                status = True
        return [counter, status]

    def elbow_plank_leg_raises(self, counter, status):
        left_foot = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_foot = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if left_foot[1] < hip_center or right_foot[1] < hip_center:
                counter += 1
                status = False
        else:
            if left_foot[1] > hip_center and right_foot[1] > hip_center:
                status = True
        return [counter, status]

    def flow_steps(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if left_knee[1] < hip_center or right_knee[1] < hip_center:
                counter += 1
                status = False
        else:
            if left_knee[1] > hip_center and right_knee[1] > hip_center:
                status = True
        return [counter, status]

    def flutter_kicks(self, counter, status):
        left_foot = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_foot = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if abs(left_foot[1] - right_foot[1]) > 0.2:
                counter += 1
                status = False
        else:
            if abs(left_foot[1] - right_foot[1]) < 0.1:
                status = True
        return [counter, status]

    def get_ups(self, counter, status):
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        shoulder_center = (self.landmarks["LEFT_SHOULDER"][1] + self.landmarks["RIGHT_SHOULDER"][1]) / 2
        if status:
            if hip_center < shoulder_center:
                counter += 1
                status = False
        else:
            if hip_center >= shoulder_center:
                status = True
        return [counter, status]

    def half_squat_walk(self, counter, status):
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        knee_center = (self.landmarks["LEFT_KNEE"][1] + self.landmarks["RIGHT_KNEE"][1]) / 2
        if status:
            if hip_center > knee_center:
                counter += 1
                status = False
        else:
            if hip_center <= knee_center:
                status = True
        return [counter, status]

    def heel_taps(self, counter, status):
        left_heel = detection_body_part(self.landmarks, "LEFT_HEEL")
        right_heel = detection_body_part(self.landmarks, "RIGHT_HEEL")
        hands = [
            detection_body_part(self.landmarks, "LEFT_WRIST"),
            detection_body_part(self.landmarks, "RIGHT_WRIST"),
    ]
        if status:
            if abs(left_heel[1] - hands[0][1]) < 0.1 or abs(right_heel[1] - hands[1][1]) < 0.1:
                counter += 1
                status = False
        else:
            if abs(left_heel[1] - hands[0][1]) > 0.2 and abs(right_heel[1] - hands[1][1]) > 0.2:
                status = True
        return [counter, status]

    def high_knees(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if left_knee[1] < hip_center or right_knee[1] < hip_center:
                counter += 1
                status = False
        else:
            if left_knee[1] > hip_center and right_knee[1] > hip_center:
                status = True
        return [counter, status]

    def high_crunches(self, counter, status):
        shoulders = [
            detection_body_part(self.landmarks, "LEFT_SHOULDER"),
            detection_body_part(self.landmarks, "RIGHT_SHOULDER"),
    ]
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if shoulders[0][1] < hip_center and shoulders[1][1] < hip_center:
                counter += 1
                status = False
        else:
            if shoulders[0][1] >= hip_center and shoulders[1][1] >= hip_center:
                status = True
        return [counter, status]

    def hop_heel_clicks(self, counter, status):
        left_heel = detection_body_part(self.landmarks, "LEFT_HEEL")
        right_heel = detection_body_part(self.landmarks, "RIGHT_HEEL")
        if status:
            if abs(left_heel[0] - right_heel[0]) < 0.1:
                counter += 1
                status = False
        else:
            if abs(left_heel[0] - right_heel[0]) > 0.3:
                status = True
        return [counter, status]

    def hundreds(self, counter, status):
        hands = [
            detection_body_part(self.landmarks, "LEFT_WRIST"),
            detection_body_part(self.landmarks, "RIGHT_WRIST"),
    ]
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if hands[0][1] < hip_center and hands[1][1] < hip_center:
                counter += 1
                status = False
        else:
            if hands[0][1] >= hip_center and hands[1][1] >= hip_center:
                status = True
        return [counter, status]

    def jump_cross_punches(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        if status:
            if left_hand[0] > right_hand[0]:
                counter += 1
                status = False
        else:
            if left_hand[0] < right_hand[0]:
                status = True
        return [counter, status]

    def jumping_jacks(self, counter, status):
        hands = [
            detection_body_part(self.landmarks, "LEFT_WRIST"),
            detection_body_part(self.landmarks, "RIGHT_WRIST"),
    ]
        feet = [
            detection_body_part(self.landmarks, "LEFT_ANKLE"),
            detection_body_part(self.landmarks, "RIGHT_ANKLE"),
    ]
        if status:
            if hands[0][0] > 0.5 and hands[1][0] < 0.5 and feet[0][0] < 0.4 and feet[1][0] > 0.6:
                counter += 1
                status = False
        else:
            if hands[0][0] < 0.5 and hands[1][0] > 0.5 and feet[0][0] > 0.4 and feet[1][0] < 0.6:
                status = True
        return [counter, status]

    def knee_to_elbow_crunches(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        if status:
            if abs(left_knee[1] - left_elbow[1]) < 0.1 or abs(right_knee[1] - right_elbow[1]) < 0.1:
                counter += 1
                status = False
        else:
            if abs(left_knee[1] - left_elbow[1]) > 0.2 and abs(right_knee[1] - right_elbow[1]) > 0.2:
                status = True
        return [counter, status]

    def lawnmowers(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if left_hand[1] < hip_center or right_hand[1] < hip_center:
                counter += 1
                status = False
        else:
            if left_hand[1] > hip_center and right_hand[1] > hip_center:
                status = True
        return [counter, status]

    def leg_raises(self, counter, status):
        left_leg = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_leg = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if left_leg[1] < hip_center or right_leg[1] < hip_center:
                counter += 1
                status = False
        else:
            if left_leg[1] >= hip_center and right_leg[1] >= hip_center:
                status = True
        return [counter, status]

    def lunge_step_ups(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if left_knee[1] < hip_center or right_knee[1] < hip_center:
                counter += 1
                status = False
        else:
            if left_knee[1] >= hip_center and right_knee[1] >= hip_center:
                status = True
        return [counter, status]

    def lunges(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_ankle = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        if status:
            if left_knee[1] > left_ankle[1] or right_knee[1] > right_ankle[1]:
                counter += 1
                status = False
        else:
            if left_knee[1] <= left_ankle[1] and right_knee[1] <= right_ankle[1]:
                status = True
        return [counter, status]

    def plank_arm_raises(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        if status:
            if left_hand[1] < right_hand[1] or right_hand[1] < left_hand[1]:
                counter += 1
                status = False
        else:
            if left_hand[1] == right_hand[1]:
                status = True
        return [counter, status]

    def pop_up_tripod(self, counter, status):
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        shoulder_center = (self.landmarks["LEFT_SHOULDER"][1] + self.landmarks["RIGHT_SHOULDER"][1]) / 2
        if status:
            if hip_center < shoulder_center:
                counter += 1
                status = False
        else:
            if hip_center >= shoulder_center:
                status = True
        return [counter, status]

    def pulse_ups(self, counter, status):
        feet = (self.landmarks["LEFT_ANKLE"][1] + self.landmarks["RIGHT_ANKLE"][1]) / 2
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if feet > hip_center:
                counter += 1
                status = False
        else:
            if feet <= hip_center:
                status = True
        return [counter, status]

    def raised_arm_circles(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        shoulder_center = (self.landmarks["LEFT_SHOULDER"][1] + self.landmarks["RIGHT_SHOULDER"][1]) / 2
        if status:
            if left_hand[1] < shoulder_center and right_hand[1] < shoulder_center:
                counter += 1
                status = False
        else:
            if left_hand[1] >= shoulder_center and right_hand[1] >= shoulder_center:
                status = True
        return [counter, status]

    def reverse_crunches(self, counter, status):
        knees = (self.landmarks["LEFT_KNEE"][1] + self.landmarks["RIGHT_KNEE"][1]) / 2
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if knees < hip_center:
                counter += 1
                status = False
        else:
            if knees >= hip_center:
                status = True
        return [counter, status]

    def roll_ups(self, counter, status):
        shoulders = (self.landmarks["LEFT_SHOULDER"][1] + self.landmarks["RIGHT_SHOULDER"][1]) / 2
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if shoulders < hip_center:
                counter += 1
                status = False
        else:
            if shoulders >= hip_center:
                status = True
        return [counter, status]

    def rotations(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        if status:
            if left_hand[0] != right_hand[0]:
                counter += 1
                status = False
        else:
            if left_hand[0] == right_hand[0]:
                status = True
        return [counter, status]

    def scissor_chops(self, counter, status):
        left_leg = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_leg = detection_body_part(self.landmarks, "RIGHT_ANKLE")
        if status:
            if left_leg[1] != right_leg[1]:
                counter += 1
                status = False
        else:
            if left_leg[1] == right_leg[1]:
                status = True
        return [counter, status]

    def seal_jacks(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        if status:
            if left_hand[0] < right_hand[0]:
                counter += 1
                status = False
        else:
            if left_hand[0] >= right_hand[0]:
                status = True
        return [counter, status]

    def shoulder_taps(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        shoulders = [
            detection_body_part(self.landmarks, "LEFT_SHOULDER"),
            detection_body_part(self.landmarks, "RIGHT_SHOULDER"),
    ]
        if status:
            if abs(left_hand[0] - shoulders[0][0]) < 0.1 or abs(right_hand[0] - shoulders[1][0]) < 0.1:
                counter += 1
                status = False
        else:
            if abs(left_hand[0] - shoulders[0][0]) > 0.2 and abs(right_hand[0] - shoulders[1][0]) > 0.2:
                status = True
        return [counter, status]

    def shrimp_squats(self, counter, status):
        knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        if status:
            if knee[1] < ankle[1]:
                counter += 1
                status = False
        else:
            if knee[1] >= ankle[1]:
                status = True
        return [counter, status]

    def side_arm_raises(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        shoulder_center = (self.landmarks["LEFT_SHOULDER"][1] + self.landmarks["RIGHT_SHOULDER"][1]) / 2
        if status:
            if left_hand[1] < shoulder_center and right_hand[1] < shoulder_center:
                counter += 1
                status = False
        else:
            if left_hand[1] >= shoulder_center and right_hand[1] >= shoulder_center:
                status = True
        return [counter, status]

    def single_leg_bridges(self, counter, status):
        left_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if left_ankle[1] < hip_center:
                counter += 1
                status = False
        else:
            if left_ankle[1] >= hip_center:
                status = True
        return [counter, status]

    def sit_up_punches(self, counter, status):
        shoulders = (self.landmarks["LEFT_SHOULDER"][1] + self.landmarks["RIGHT_SHOULDER"][1]) / 2
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if shoulders < hip_center:
                counter += 1
                status = False
        else:
            if shoulders >= hip_center:
                status = True
        return [counter, status]

    def sit_ups(self, counter, status):
        shoulders = (self.landmarks["LEFT_SHOULDER"][1] + self.landmarks["RIGHT_SHOULDER"][1]) / 2
        hip_center = (self.landmarks["LEFT_HIP"][1] + self.landmarks["RIGHT_HIP"][1]) / 2
        if status:
            if shoulders < hip_center:
                counter += 1
                status = False
        else:
            if shoulders >= hip_center:
                status = True
        return [counter, status]

    def sitting_twists(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        hip_center = (self.landmarks["LEFT_HIP"][0] + self.landmarks["RIGHT_HIP"][0]) / 2
        if status:
            if abs(left_hand[0] - hip_center) < 0.2 or abs(right_hand[0] - hip_center) < 0.2:
                counter += 1
                status = False
        else:
            if abs(left_hand[0] - hip_center) > 0.3 and abs(right_hand[0] - hip_center) > 0.3:
                status = True
        return [counter, status]

    def skiers(self, counter, status):
        left_foot = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_foot = detection_body_part(self.landmarks, "RIGHT_ANKLE")

        if status:
            if abs(left_foot[0] - right_foot[0]) > 0.4:
                counter += 1
                status = False
        else:
            if abs(left_foot[0] - right_foot[0]) < 0.2:
                status = True

        return [counter, status]

    def speed_bag_punches(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")

        if status:
            if abs(left_hand[0] - right_hand[0]) < 0.1:
                counter += 1
                status = False
        else:
            if abs(left_hand[0] - right_hand[0]) > 0.3:
                status = True

        return [counter, status]

    def squat_step_ups(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")

        if status:
            if left_knee[1] < right_knee[1]:
                counter += 1
                status = False
        else:
            if left_knee[1] > right_knee[1]:
                counter += 1
                status = True

        return [counter, status]

    def star_jumps(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")
        left_foot = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_foot = detection_body_part(self.landmarks, "RIGHT_ANKLE")

        if status:
            if (left_hand[1] < 0.4 and right_hand[1] < 0.4) and (left_foot[0] < 0.2 and right_foot[0] > 0.8):
                counter += 1
                status = False
        else:
            if (left_hand[1] > 0.6 and right_hand[1] > 0.6):
                status = True

        return [counter, status]

    def straight_leg_bounds(self, counter, status):
        left_foot = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_foot = detection_body_part(self.landmarks, "RIGHT_ANKLE")

        if status:
            if abs(left_foot[1] - right_foot[1]) < 0.2:
                counter += 1
                status = False
        else:
            if abs(left_foot[1] - right_foot[1]) > 0.4:
                status = True

        return [counter, status]

    def sumo_squats(self, counter, status):
        hip_angle = self.angle_of_the_hip()

        if status:
            if hip_angle < 70:
                counter += 1
                status = False
        else:
            if hip_angle > 160:
                status = True

        return [counter, status]

    def superman_v(self, counter, status):
        nose = detection_body_part(self.landmarks, "NOSE")
        pelvis = detection_body_part(self.landmarks, "PELVIS")

        if status:
            if nose[1] < pelvis[1]:
                counter += 1
                status = False
        else:
            if nose[1] > pelvis[1]:
                status = True

        return [counter, status]

    def toe_taps(self, counter, status):
        left_foot = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_foot = detection_body_part(self.landmarks, "RIGHT_ANKLE")

        if status:
            if left_foot[1] < 0.5 or right_foot[1] < 0.5:
                counter += 1
                status = False
        else:
            if left_foot[1] > 0.7 and right_foot[1] > 0.7:
                status = True

        return [counter, status]

    def twist_jacks(self, counter, status):
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        right_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")

        if status:
            if abs(left_shoulder[0] - right_shoulder[0]) > 0.5:
                counter += 1
                status = False
        else:
            if abs(left_shoulder[0] - right_shoulder[0]) < 0.3:
                status = True

        return [counter, status]

    def twists(self, counter, status):
        torso_angle = self.angle_of_the_torso()

        if status:
            if abs(torso_angle) > 30:
                counter += 1
                status = False
        else:
            if abs(torso_angle) < 10:
                status = True

        return [counter, status]

    def updown_planks(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")

        if status:
            if left_hand[1] > 0.5 and right_hand[1] > 0.5:
                counter += 1
                status = False
        else:
            if left_hand[1] < 0.3 and right_hand[1] < 0.3:
                status = True

        return [counter, status]

    def v_ups(self, counter, status):
        torso_angle = self.angle_of_the_torso()
        leg_angle = self.angle_of_the_leg()

        if status:
            if torso_angle < 45 and leg_angle < 45:
                counter += 1
                status = False
        else:
            if torso_angle > 100 and leg_angle > 100:
                status = True

        return [counter, status]

    def wide_grip(self, counter, status):
        left_hand = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_hand = detection_body_part(self.landmarks, "RIGHT_WRIST")

        if status:
            if abs(left_hand[0] - right_hand[0]) > 0.6:
                counter += 1
                status = False
        else:
            if abs(left_hand[0] - right_hand[0]) < 0.4:
                status = True

        return [counter, status]

    def windshield_wipers(self, counter, status):
        left_foot = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_foot = detection_body_part(self.landmarks, "RIGHT_ANKLE")

        if status:
            if abs(left_foot[0] - right_foot[0]) > 0.5:
                counter += 1
                status = False
        else:
            if abs(left_foot[0] - right_foot[0]) < 0.3:
                status = True

        return [counter, status]

    def jumping_jacks(self, counter, status):
        left_wrist = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_wrist = detection_body_part(self.landmarks, "RIGHT_WRIST")
        left_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        right_ankle = detection_body_part(self.landmarks, "RIGHT_ANKLE")

        avg_hand_height = (left_wrist[1] + right_wrist[1]) / 2
        avg_foot_height = (left_ankle[1] + right_ankle[1]) / 2

        if status:
            if avg_hand_height > avg_foot_height:  
                counter += 1
                status = False
        else:
            if avg_hand_height < avg_foot_height:  
                status = True

        return [counter, status]
    
    def plank(self, counter, status):
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        right_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
        left_hip = detection_body_part(self.landmarks, "LEFT_HIP")
        right_hip = detection_body_part(self.landmarks, "RIGHT_HIP")

        avg_hip_height = (left_hip[1] + right_hip[1]) / 2
        avg_shoulder_height = (left_shoulder[1] + right_shoulder[1]) / 2

        if avg_hip_height > avg_shoulder_height:
            status = True 
        else:
            status = False

        return [counter, status]
    
    def high_knees(self, counter, status):
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_hip = detection_body_part(self.landmarks, "LEFT_HIP")
        right_hip = detection_body_part(self.landmarks, "RIGHT_HIP")

        avg_hip_height = (left_hip[1] + right_hip[1]) / 2

        if status:
            if left_knee[1] < avg_hip_height or right_knee[1] < avg_hip_height:
                counter += 1
                status = False
        else:
            if left_knee[1] > avg_hip_height and right_knee[1] > avg_hip_height:
                status = True

        return [counter, status]
    
    def calculate_exercise(self, exercise_type, counter, status):
        if exercise_type == "push-up":
            counter, status = TypeOfExercise(self.landmarks).push_up(
                counter, status)
        elif exercise_type == "pull-up":
            counter, status = TypeOfExercise(self.landmarks).pull_up(
                counter, status)
        elif exercise_type == "squat":
            counter, status = TypeOfExercise(self.landmarks).squat(
                counter, status)
        elif exercise_type == "walk":
            counter, status = TypeOfExercise(self.landmarks).walk(
                counter, status)
        elif exercise_type == "sit-up":
            counter, status = TypeOfExercise(self.landmarks).sit_up(
                counter, status)
        elif exercise_type == " Army-Crawl":
            counter, status = TypeOfExercise(self.landmarks).army_crawl(
                counter, status)
        elif exercise_type == "Bounces":
            counter, status = TypeOfExercise(self.landmarks).bounces(
                counter, status)
        elif exercise_type == "Crunches":
            counter, status = TypeOfExercise(self.landmarks).crunches(
                counter, status)
        elif exercise_type == "L-Sit-Ups":
            counter, status = TypeOfExercise(self.landmarks).l_sit_ups(
                counter, status)
        elif exercise_type == "Pop-Up-Tripod":
            counter, status = TypeOfExercise(self.landmarks).pop_up_tripod(
                counter, status)
        elif exercise_type == " Raised-Leg-Crunches":
            counter, status = TypeOfExercise(self.landmarks).raised_leg_crunches(
                counter, status)
        elif exercise_type == "Scissors":
            counter, status = TypeOfExercise(self.landmarks).scissors(
                counter, status)
        elif exercise_type == "Sit-Up-Elbow-Strikes":
            counter, status = TypeOfExercise(self.landmarks).sit_up_elbow_strikes(
                counter, status)
        elif exercise_type == "Sitting-Punches":
            counter, status = TypeOfExercise(self.landmarks).sitting_punches(
                counter, status)
        elif exercise_type == "Superman":
            counter, status = TypeOfExercise(self.landmarks).superman(
                counter, status)
        elif exercise_type == "Thigh-Taps":
            counter, status = TypeOfExercise(self.landmarks).thigh_taps(
                counter, status)
        elif exercise_type == "Accordion-Push-Ups":
            counter, status = TypeOfExercise(self.landmarks).accordion_push_ups(
                counter, status)
        elif exercise_type == "Air-Bike-Crunches":
            counter, status = TypeOfExercise(self.landmarks).air_bike_crunches(
                counter, status)
        elif exercise_type == "Balance-Side-Lunges":
            counter, status = TypeOfExercise(self.landmarks).balance_side_lunges(
                counter, status)
        elif exercise_type == "Bear-Crawl":
            counter, status = TypeOfExercise(self.landmarks).bear_crawl(
                counter, status)
        elif exercise_type == "Body-Saw":
            counter, status = TypeOfExercise(self.landmarks).body_saw(
                counter, status)
        elif exercise_type == "Burpees-with-a-Push-Up":
            counter, status = TypeOfExercise(self.landmarks).burpees_with_push_up(
                counter, status)
        elif exercise_type == "Burpees-with-Rotations":
            counter, status = TypeOfExercise(self.landmarks).burpees_with_rotations(
                counter, status)
        elif exercise_type == "Burpees":
            counter, status = TypeOfExercise(self.landmarks).burpees(
                counter, status)
        elif exercise_type == "Butt-Kicks":
            counter, status = TypeOfExercise(self.landmarks).butt_kicks(
                counter, status)
        elif exercise_type == "Calf-Raises":
            counter, status = TypeOfExercise(self.landmarks).calf_raises(
                counter, status)
        elif exercise_type == "Chest-Expansions":
            counter, status = TypeOfExercise(self.landmarks).chest_expansions(
                counter, status)
        elif exercise_type == "Climber-Taps":
            counter, status = TypeOfExercise(self.landmarks).climber_taps(
                counter, status)
        elif exercise_type == "Climbers":
            counter, status = TypeOfExercise(self.landmarks).climbers(
                counter, status)
        elif exercise_type == "Close-Grip":
            counter, status = TypeOfExercise(self.landmarks).close_grip(
                counter, status)
        elif exercise_type == "Curtsy-Lunges":
            counter, status = TypeOfExercise(self.landmarks).curtsy_lunges(
                counter, status)
        elif exercise_type == "Dragon-Push-Ups":
            counter, status = TypeOfExercise(self.landmarks).dragon_push_ups(
                counter, status)
        elif exercise_type == "Dynamic-Squats":
            counter, status = TypeOfExercise(self.landmarks).dynamic_squats(
                counter, status)
        elif exercise_type == "Elbow-Plank-Leg-Raises":
            counter, status = TypeOfExercise(self.landmarks).elbow_plank_leg_raises(
                counter, status)
        elif exercise_type == "Flow-Steps":
            counter, status = TypeOfExercise(self.landmarks).flow_steps(
                counter, status)
        elif exercise_type == "Flutter-Kicks":
            counter, status = TypeOfExercise(self.landmarks).flutter_kicks(
                counter, status)
        elif exercise_type == "Get-Ups":
            counter, status = TypeOfExercise(self.landmarks).get_ups(
                counter, status)
        elif exercise_type == "Half-Squat-Walk":
            counter, status = TypeOfExercise(self.landmarks).half_squat_walk(
                counter, status)
        elif exercise_type == "Heel-Taps":
            counter, status = TypeOfExercise(self.landmarks).heel_taps(
                counter, status)
        elif exercise_type == "High-Knees":
            counter, status = TypeOfExercise(self.landmarks).high_knees(
                counter, status)
        elif exercise_type == "High-Crunches":
            counter, status = TypeOfExercise(self.landmarks).high_crunches(
                counter, status)
        elif exercise_type == "Hop-Heel-Clicks":
            counter, status = TypeOfExercise(self.landmarks).hop_heel_clicks(
                counter, status)
        elif exercise_type == "Hundreds":
            counter, status = TypeOfExercise(self.landmarks).hundreds(
                counter, status)
        elif exercise_type == "Jump-Cross-Punches":
            counter, status = TypeOfExercise(self.landmarks).jump_cross_punches(
                counter, status)
        elif exercise_type == "Jumping-Jacks":
            counter, status = TypeOfExercise(self.landmarks).jumping_jacks(
                counter, status)
        elif exercise_type == "Knee-to-Elbow-Crunches":
            counter, status = TypeOfExercise(self.landmarks).knee_to_elbow_crunches(
                counter, status)
        elif exercise_type == "Lawnmowers":
            counter, status = TypeOfExercise(self.landmarks).lawnmowers(
                counter, status)
        elif exercise_type == "Leg-Raises":
            counter, status = TypeOfExercise(self.landmarks).leg_raises(
                counter, status)
        elif exercise_type == "Lunge-Step-Ups":
            counter, status = TypeOfExercise(self.landmarks).lunge_step_ups(
                counter, status)
        elif exercise_type == "Lunges":
            counter, status = TypeOfExercise(self.landmarks).lunges(
                counter, status)
        elif exercise_type == "Plank-Arm-Raises":
            counter, status = TypeOfExercise(self.landmarks).plank_arm_raises(
                counter, status)
        elif exercise_type == "Pop-Up-Tripod":
            counter, status = TypeOfExercise(self.landmarks).pop_up_tripod(
                counter, status)
        elif exercise_type == "pulse-Ups":
            counter, status = TypeOfExercise(self.landmarks).pulse_ups(
                counter, status)
        elif exercise_type == "Pulse-Ups":
            counter, status = TypeOfExercise(self.landmarks).pulse_ups(
                counter, status)
        elif exercise_type == "Raised-Arm-Circles":
            counter, status = TypeOfExercise(self.landmarks).raised_arm_circles(
                counter, status)
        elif exercise_type == "Reverse-Crunches":
            counter, status = TypeOfExercise(self.landmarks).reverse_crunches(
                counter, status)
        elif exercise_type == "Roll-Ups":
            counter, status = TypeOfExercise(self.landmarks).roll_ups(
                counter, status)
        elif exercise_type == "Rotations":
            counter, status = TypeOfExercise(self.landmarks).rotations(
                counter, status)
        elif exercise_type == "Scissor-Chops":
            counter, status = TypeOfExercise(self.landmarks).scissor_chops(
                counter, status)
        elif exercise_type == "Seal-Jacks":
            counter, status = TypeOfExercise(self.landmarks).seal_jacks(
                counter, status)
        elif exercise_type == "Shoulder-Taps":
            counter, status = TypeOfExercise(self.landmarks).shoulder_taps(
                counter, status)
        elif exercise_type == "Shrimp-Squats":
            counter, status = TypeOfExercise(self.landmarks).shrimp_squats(
                counter, status)
        elif exercise_type == "Side-Arm-Raises":
            counter, status = TypeOfExercise(self.landmarks).side_arm_raises(
                counter, status)
        elif exercise_type == "Single-Leg-Bridges":
            counter, status = TypeOfExercise(self.landmarks).single_leg_bridges(
                counter, status)
        elif exercise_type == "Sit-Up-Punches":
            counter, status = TypeOfExercise(self.landmarks).sit_up_punches(
                counter, status)
        elif exercise_type == "Sit-Ups":
            counter, status = TypeOfExercise(self.landmarks).sit_ups(
                counter, status)
        elif exercise_type == "Sitting-Twists":
            counter, status = TypeOfExercise(self.landmarks).sitting_twists(
                counter, status)
        elif exercise_type == "Skiers":
            counter, status = TypeOfExercise(self.landmarks).skiers(
                counter, status)
        elif exercise_type == "Speed-Bag-Punches":
            counter, status = TypeOfExercise(self.landmarks).speed_bag_punches(
                counter, status)
        elif exercise_type == "Squat-Step-Ups":
            counter, status = TypeOfExercise(self.landmarks).squat_step_ups(
                counter, status)
        elif exercise_type == "Star-Jumps":
            counter, status = TypeOfExercise(self.landmarks).star_jumps(
                counter, status)
        elif exercise_type == "Straight-Leg-Bounds":
            counter, status = TypeOfExercise(self.landmarks).straight_leg_bounds(
                counter, status)
        elif exercise_type == "Sumo-Squats":
            counter, status = TypeOfExercise(self.landmarks).sumo_squats(
                counter, status)
        elif exercise_type == "Superman-V":
            counter, status = TypeOfExercise(self.landmarks).superman_v(
                counter, status)
        elif exercise_type == "Toe-Taps":
            counter, status = TypeOfExercise(self.landmarks).toe_taps(
                counter, status)
        elif exercise_type == "Twist-Jacks":
            counter, status = TypeOfExercise(self.landmarks).twist_jacks(
                counter, status)
        elif exercise_type == "Twists":
            counter, status = TypeOfExercise(self.landmarks).twists(
                counter, status)
        elif exercise_type == "UpDown-Planks":
            counter, status = TypeOfExercise(self.landmarks).updown_planks(
                counter, status)
        elif exercise_type == "V-Ups":
            counter, status = TypeOfExercise(self.landmarks).v_ups(
                counter, status)
        elif exercise_type == "Wide-Grip":
            counter, status = TypeOfExercise(self.landmarks).wide_grip(
                counter, status)
        elif exercise_type == "Windshield-Wipers":
            counter, status = TypeOfExercise(self.landmarks).windshield_wipers(
                counter, status)
        return [counter, status]
