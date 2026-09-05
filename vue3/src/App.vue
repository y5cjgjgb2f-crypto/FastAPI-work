<template>
  <div>
    <div style="text-align: center; font-size: 30px; margin-bottom: 20px; font-weight: bold">学习FastAPI + Vue3</div>
    <div style="text-align: center; margin-bottom: 50px; font-size: 18px">学生信息管理页面（增删改查）</div>
    <div style="width: 70%; margin: 30px auto">
      <div style="margin-bottom: 10px">
        <el-input clearable @clear="load" style="width: 300px" v-model="data.name" placeholder="请输入姓名查询"></el-input>
        <el-button type="info" @click="load" style="margin-left: 5px; margin-right: 20px">搜索</el-button>
        <el-button type="primary" @click="handleAdd">新增</el-button>
      </div>

      <div>
        <el-table border stripe :data="data.tableData" style="width: 100%">
          <el-table-column prop="no" label="学号" />
          <el-table-column prop="name" label="姓名" />
          <el-table-column prop="clazz" label="班级" />
          <el-table-column prop="major" label="专业" />
          <el-table-column prop="college" label="学院" />
          <el-table-column prop="phone" label="手机" />
          <el-table-column prop="email" label="邮箱" />
          <el-table-column prop="address" label="地址" />
          <el-table-column label="操作">
            <template #default="scope">
              <el-button size="small" type="primary" @click="handleEdit(scope.row)">编辑</el-button>
              <el-button size="small" type="danger" @click="remove()">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div style="margin-top: 10px">
        <el-pagination background layout="total, prev, pager, next" @current-change="load" v-model:current-page="data.pageNum"
                       v-model:page-size="data.pageSize" :total="data.total" />
      </div>
    </div>
  </div>
</template>


<script setup>
import {reactive} from "vue";

const data = reactive({
  name: null,
  pageNum: 1,
  pageSize: 2,
  total: 4,
  tableData: []
})

const handleAdd = () => {
  // 新增数据
}

const handleEdit = (row) => {
  // 编辑行数据
  console.log(row)
}

const remove = (id) => {
  // 根据ID删除数据
}

const load = () => {
  data.tableData = [
      { no: '20231001', name: '小林1', clazz: '计科1班', major: '计算机科学与技术', college: '计算机学院', phone: '13899887766',
      email: 'xiaolin@163.com', address: '安徽合肥' },
    { no: '20231002', name: '小林2', clazz: '计科1班', major: '计算机科学与技术', college: '计算机学院', phone: '13899887766',
      email: 'xiaolin@163.com', address: '安徽合肥' },
    { no: '20231003', name: '小林3', clazz: '计科1班', major: '计算机科学与技术', college: '计算机学院', phone: '13899887766',
      email: 'xiaolin@163.com', address: '安徽合肥' },
    { no: '20231004', name: '小林4', clazz: '计科1班', major: '计算机科学与技术', college: '计算机学院', phone: '13899887766',
      email: 'xiaolin@163.com', address: '安徽合肥' },
  ]
}
load()  // 加载数据
</script>


<style scoped>

</style>
