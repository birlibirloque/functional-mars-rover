(ns mars-rovers
  (:require [clojure.test :refer :all]))

(defn- make-direction [value left right x y]
  {:value value :left left :right right :x x :y y})

(def ^:private directions {"N" (make-direction "N" "W" "E" 0 1)
                           "S" (make-direction "S" "E" "W" 0 -1)
                           "E" (make-direction "E" "N" "S" 1 0)
                           "W" (make-direction "W" "S" "N" -1 0)})

(defn make-rover [x y direction-type]
  {:x x :y y :direction (directions direction-type)})

(defn- turn [new-direction {:keys [direction] :as rover} & args]
  (assoc rover :direction (-> new-direction direction directions)))

(defn- warp-if-needed [position]
  (get {-1 100 101 0} position position))

(defn- new-position [coordinate {:keys [direction] :as rover} operation]
  (warp-if-needed (operation (rover coordinate)
                             (direction coordinate))))

(defn- is-there-any-obstacle-in? [coordinate position obstacles]
  (some #(= position (coordinate %)) obstacles))

(defn- calculate-change [rover coordinate position obstacles]
  (if (is-there-any-obstacle-in? coordinate position obstacles)
    (coordinate rover)
    position))

(defn- change [coordinate operation obstacles rover]
  (let [position (new-position coordinate rover operation)]
    (assoc rover coordinate (calculate-change rover coordinate position obstacles))))

(defn- move [operation rover obstacles]
  (->> rover
       (change :x operation obstacles)
       (change :y operation obstacles)))

(def ^:private all-commands {"L" (partial turn :left) "R" (partial turn :right)
                             "F" (partial move +) "B" (partial move -)})

(defn- execute-command [obstacles]
  (fn [rover command]
    ((all-commands command) rover obstacles)))

(defn move-rover [{:keys [x y direction commands obstacles] :or {obstacles []}}]
  (reduce (execute-command obstacles)
          (make-rover x y direction)
          (map str commands)))


(deftest rover-movement
  (testing "moving forward"
    (is (= 1 (:y (move-rover {:x 0 :y 0 :direction "N" :commands "F"}))))
    (is (= 2 (:y (move-rover {:x 0 :y 0 :direction "N" :commands "FF"})))))

  (testing "moving backwards"
    (is (= 0 (:y (move-rover {:x 0 :y 1 :direction "N" :commands "B"})))))

  (testing "rotation"
    (is (= "E" (get-in (move-rover {:x 0 :y 0 :direction "N" :commands "R"}) [:direction :value])))
    (is (= "W" (get-in (move-rover {:x 0 :y 0 :direction "N" :commands "L"}) [:direction :value])))
    (is (= "S" (get-in (move-rover {:x 0 :y 0 :direction "N" :commands "RR"}) [:direction :value])))
    (is (= "S" (get-in (move-rover {:x 0 :y 0 :direction "N" :commands "LL"}) [:direction :value])))
    (is (= "N" (get-in (move-rover {:x 0 :y 0 :direction "N" :commands "LLLL"}) [:direction :value]))))

  (testing "movement facing east"
    (is (= 1 (:x (move-rover {:x 0 :y 0 :direction "N" :commands "RF"})))))

  (testing "movement facing west"
    (is (= 11 (:x (move-rover {:x 10 :y 5 :direction "W" :commands "FBB"})))))

  (testing "movement facing south"
    (is (= 1 (:y (move-rover {:x 0 :y 0 :direction "N" :commands "LLB"})))))

  (testing "planet is round"
    (is (= 100 (:y (move-rover {:x 0 :y 0 :direction "N" :commands "B"}))))
    (is (= 0 (:y (move-rover {:x 0 :y 100 :direction "N" :commands "F"}))))
    (is (= 100 (:x (move-rover {:x 0 :y 34 :direction "W" :commands "F"}))))
    (is (= 0 (:x (move-rover {:x 100 :y 34 :direction "E" :commands "F"})))))

  (testing "collision"
    (is (= 0 (:y (move-rover {:x 0 :y 0 :direction "N" :commands "F" :obstacles [{:x 0 :y 1}]}))))
    (is (= 0 (:y (move-rover {:x 0 :y 0 :direction "N" :commands "B" :obstacles [{:x 0 :y 100}]}))))
    (is (= 1 (:y (move-rover {:x 0 :y 0 :direction "N" :commands "BF" :obstacles [{:x 0 :y 100}]})))))
  )
