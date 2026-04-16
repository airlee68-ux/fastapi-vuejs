<template>
  <div class="layout">
    <header>
      <slot name="header">
        <h1>게시판</h1>
      </slot>
    </header>
    <main>
      <slot></slot>
    </main>
  </div>
</template>

<style scoped>
.layout {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
header {
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #eee;
}
</style>
