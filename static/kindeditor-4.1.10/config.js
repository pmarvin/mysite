/**
 * Created by Administrator on 2017/7/2.
 */
KindEditor.ready(function (K) {
    K.create('#textarea[name=content]',{
        width:'800',
        height:'400',
        /**设置上传路径**/
        uploadJson:'/admin/upload/kindeditor',
    });
});