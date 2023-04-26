<script setup>
import PostRequirement from './components/PostRequirement.vue';
</script>

<template>
    <div>
    <el-container>
      <el-header>Moonshot Service Learning</el-header>
      <el-main><PostRequirement /></el-main>
    </el-container>
      
    </div>
</template>

<style scoped>
  .el-header{
    /* background-color: #E9EEF3;
    color: #409EFF; */
    text-align: left;
    line-height: 60px;
    font-size: 30px;
    font-weight: bold;
  }
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
  }
</style>