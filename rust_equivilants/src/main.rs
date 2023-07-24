use pandas_rs::prelude::*;
fn main() {

    let df = 
        Pd::read_csv("../machine_learning_course/data/train.csv")
        .unwrap();

    let sales = Pd::get_column(&df, "SalePrice");
    sales[1..15].to_vec().display();





}
