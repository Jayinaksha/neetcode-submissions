use std::collections::HashMap;
impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut memory: HashMap<i32,i32> = HashMap::new();

        for num in nums{
            *memory.entry(num).or_insert(0) += 1;
        }
        let mut count_vec: Vec<(i32,i32)> = memory.into_iter().collect();
        count_vec.sort_by(|a,b| b.1.cmp(&a.1));
        count_vec.into_iter()
            .take(k as usize)
            .map(|(num, _count)| num)
            .collect()
   
    }
}
