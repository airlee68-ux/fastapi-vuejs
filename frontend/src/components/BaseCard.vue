<template>
  <div class="card">
    <div class="card-header">
      <slot name="header">기본 제목</slot>
    </div>
    <div class="card-body">
      <slot></slot>
    </div>
    <div class="card-footer">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<style scoped>
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 16px;
}
.card-header {
  background: #f5f5f5;
  padding: 12px 16px;
  font-weight: bold;
}
.card-body {
  padding: 16px;
}
.card-footer {
  background: #f5f5f5;
  padding: 12px 16px;
  text-align: right;
}
</style>
