impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hash = HashMap::new();
        for (i, &num) in nums.iter().enumerate() {
            let diff = target - num;
            if  let Some(&prev_idx) = hash.get(&diff) {
                return vec![prev_idx as i32, i as i32];
            }
            hash.insert(num, i);
        }
        vec![]
    }
}
