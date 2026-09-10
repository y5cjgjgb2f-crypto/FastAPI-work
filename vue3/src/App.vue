<template>
  <div>
    <div style="text-align: center; font-size: 30px; margin-bottom: 20px; font-weight: bold">FastAPI + Vue3</div>
    <div style="text-align: center; margin-bottom: 50px; font-size: 18px">学生信息管理页面（增删改查）</div>
    <div style="width: 70%; margin: 30px auto">
      <div style="margin-bottom: 10px">
        <el-input clearable @clear="load" style="width: 300px; margin-right: 5px" v-model="data.no" placeholder="请输入学号查询"></el-input>
        <el-input clearable @clear="load" style="width: 300px" v-model="data.name" placeholder="请输入姓名查询"></el-input>
        <el-button type="info" @click="load" style="margin-left: 5px; margin-right: 20px">搜索</el-button>
        <el-button type="primary" @click="handleAdd">新增</el-button>
      </div>

      <div>
        <el-table border stripe :data="data.tableData" style="width: 100%">
          <el-table-column prop="id" label="ID" width="70" />
          <el-table-column prop="no" label="学号" />
          <el-table-column prop="name" label="姓名" />
          <el-table-column prop="clazz" label="班级" />
          <el-table-column prop="major" label="专业" />
          <el-table-column prop="college" label="学院" />
          <el-table-column prop="phone" label="手机号" />
          <el-table-column prop="email" label="邮箱" />
          <el-table-column prop="address" label="地址" />
          <el-table-column label="操作" width="150">
            <template #default="scope">
              <el-button size="small" type="primary" @click="handleEdit(scope.row)">编辑</el-button>
              <el-button size="small" type="danger" @click="remove(scope.row.id)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div style="margin-top: 10px">
        <el-pagination background layout="total, prev, pager, next" @current-change="load" v-model:current-page="data.pageNum"
                       v-model:page-size="data.pageSize" :total="data.total" />
      </div>
    </div>

    <el-dialog v-model="data.dialogVisible" title="学生信息" width="30%" destroy-on-close>
      <el-form ref="formRef" :model="data.form" :rules="data.rules" label-width="70px" style="padding: 20px">
        <el-form-item prop="no" label="学号">
          <el-input :disabled="data.form.id > 0" v-model="data.form.no" autocomplete="off" placeholder="请输入学号" />
        </el-form-item>
        <el-form-item prop="name" label="姓名">
          <el-input v-model="data.form.name" autocomplete="off" placeholder="请输入姓名" />
        </el-form-item>
        <el-form-item prop="clazz" label="班级">
          <el-input v-model="data.form.clazz" autocomplete="off" placeholder="请输入班级" />
        </el-form-item>
        <el-form-item prop="major" label="专业">
          <el-input v-model="data.form.major" autocomplete="off" placeholder="请输入专业" />
        </el-form-item>
        <el-form-item prop="college" label="学院">
          <el-input v-model="data.form.college" autocomplete="off" placeholder="请输入学院" />
        </el-form-item>
        <el-form-item prop="phone" label="手机号">
          <el-input v-model="data.form.phone" autocomplete="off" placeholder="请输入手机号" />
        </el-form-item>
        <el-form-item prop="email" label="邮箱">
          <el-input v-model="data.form.email" autocomplete="off" placeholder="请输入邮箱" />
        </el-form-item>
        <el-form-item prop="address" label="地址">
          <el-input type="textarea" v-model="data.form.address" autocomplete="off" placeholder="请输入地址" />
        </el-form-item>
      </el-form>
      <template #footer>
          <div class="dialog-footer">
            <el-button @click="data.dialogVisible = false">取消</el-button>
            <el-button type="primary" @click="save">保存</el-button>
          </div>
        </template>
    </el-dialog>

  </div>
</template>


<script setup>
import {reactive, ref} from "vue";
import axios from "axios";
import {ElMessage, ElMessageBox} from "element-plus";

const formRef = ref()
const ip = "/api"
const data = reactive({
  no: null,
  name: null,
  pageNum: 1,
  pageSize: 5,
  total: 0,
  tableData: [],
  dialogVisible: false,
  form: {},
  rules: {
    no: [
      { required: true, message: '请输入学号', trigger: 'blur' }
    ],
    name: [
      { required: true, message: '请输入姓名', trigger: 'blur' }
    ]
  }
})

const handleAdd = () => {
  // 新增数据
  data.dialogVisible = true
  data.form = {}
}

const handleEdit = (row) => {
  data.form = JSON.parse(JSON.stringify(row))  // 深拷贝
  data.dialogVisible = true
}

const add = () => {
  axios.post(ip + '/student/add', data.form).then(res => {
    if (res.status === 200) {  //成功
      data.dialogVisible = false  // 关闭弹窗
      load()
      ElMessage.success('新增成功')
    } else {
      ElMessage.error('新增失败')
    }
  })
}

const update = () => {
  axios.put(ip + '/student/update', data.form).then(res => {
    if (res.status === 200) {  //成功
      data.dialogVisible = false  // 关闭弹窗
      load()
      ElMessage.success('修改成功')
    } else {
      ElMessage.error('修改失败')
    }
  })
}

const save = () => {
  formRef.value.validate(valid => {
    if (valid) {  // 验证通过
      if (data.form.id) {  // 编辑
        update()
      } else {  // 新增
        add()
      }
    }
  })
}

const remove = (id) => {
  ElMessageBox.confirm('删除后数据无法恢复，确定删除吗？', '删除确认', { type: 'warning' }).then(res => {
    // 根据ID删除数据
    axios.delete(ip + '/student/delete/' + id).then(res => {
      if (res.status === 200) {  //成功
        load()
        ElMessage.success('删除成功')
      } else {
        ElMessage.error('删除失败')
      }
    })
  }).catch(err => {})
}

const load = () => {
  axios.get(ip + '/student/selectPage', {
    params: {
      pageNum: data.pageNum,
      pageSize: data.pageSize,
      no: data.no,
      name: data.name
    }
  }).then(res => {
    data.tableData = res.data.list
    data.total = res.data.total
  })
}
load()  // 加载数据
</script>


<style scoped>

</style>
