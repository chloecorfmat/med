<template>
    <div>
        <Menu />
    </div>
</template>

<script>
  import Menu from '@/components/Menu';
  export default {
    name: 'Logout',
    components: { Menu },
    created() {
      this.$session.destroy()
      this.$router.push('/login')
    }
  }
</script>
