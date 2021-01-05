# 退款业务类数据定义

1.退款申请
前端=>后端
{
    type_of_refund: '',
    amount_of_refund: '',
    status_of_goods: '',
    way_of_refund: '',
    reason_of_refund: '',
    fileList: []
}

后端=>前端
{
    status_of_order表示订单状态，0和1表示退单和未退单
    Image: '',
    class_of_commidity: '',
    seller: '',
    method_of_pay: '',
    name_of_commidity: '',
    price_of_commidity: '',
    real_price_of_commidity: ''
}

说明：
    Image：商品图像；
    name_of_commidity表示商品名称；
    class_of_commidity表示商品类别；
    price_of_commidity表示商品的标价；
    real_price_of_commidity表示商品的实际付价；
    method_of_pay表示支付方式；
    seller表示卖家；
    type_of_refund表示退款类型；
    amount_of_refund表示退款金额；
    status_of_goods表示货物状态；
    way_of_refund表示退货方式；
    reason_of_refund表示退款原因；
    filelist表示退款补充说明上传的图像组



2.退款审核
前端=>后端
{
    status_of_order: ''
}
后端=>前端
{
    status_of_order表示订单状态，0和1表示退单和未退单
    type_of_refund: '',
    amount_of_refund: '',
    status_of_goods: '',
    way_of_refund: '',
    reason_of_refund: '',
    Image: '',
    class_of_commidity: '',
    seller: '',
    method_of_pay: '',
    name_of_commidity: '',
    price_of_commidity: '',
    real_price_of_commidity: '',
    fileList: []
}

说明：
    status_of_order表示订单状态，0和1表示已退单和未退单
    Image表示商品图像；
    name_of_commidity表示商品名称；
    class_of_commidity表示商品类别；
    price_of_commidity表示商品的标价；
    real_price_of_commidity表示商品的实际付价；
    method_of_pay表示支付方式；
    seller表示卖家；
    type_of_refund表示退款类型；
    amount_of_refund表示退款金额；
    status_of_goods表示货物状态；
    way_of_refund表示退货方式；
    reason_of_refund表示退款原因；
    filelist表示退款补充说明上传的图像组

