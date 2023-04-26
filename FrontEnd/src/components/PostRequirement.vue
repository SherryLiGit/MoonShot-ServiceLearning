<script setup>
import { reactive } from 'vue'
import axios from 'axios'

const requirement = reactive({
  Email: '',
  ActivityName: '',
  Introduction: '',
  VolunteerNumber: '',
})

const onSubmit = () => {
  console.log('submit!')
  axios({
    // 默认请求方式为get
    method: 'post',
    url: '/api/postRequirement',
    // 传递参数
    data: {
      ActivityName: requirement.ActivityName,
      Introduction: requirement.Introduction
    },
    responseType: 'json'
  }).then(response => {
    console.log(response)
  }).catch(error => {
    console.log("error")
  });
}




</script>


<template>
  <div>
    <el-card class="box-card" style="width: 60%; margin: auto;">
      <template #header>
        <div class="card-header">
          <span>清森探月社会服务活动发布表</span>
        </div>
      </template>
      <div>
        <el-form :model="requirement" label-width="120px" label-position="top">
          <el-form-item label="您的邮箱 Your Email">
            <el-input v-model="requirement.Email" />
          </el-form-item>
          <el-form-item label="社会服务名称 The Name of Service Learning">
            <el-input v-model="requirement.ActivityName" />
          </el-form-item>
          <el-form-item label="社会服务简介 Introduction to Service Learning">
            <el-input v-model="requirement.Introduction" type="textarea" />
          </el-form-item>
          <el-form-item label="预计招募人数 Estimated Number of Recruits">
            <el-input v-model="requirement.VolunteerNumber" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">提交</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-card>
  </div>
</template>