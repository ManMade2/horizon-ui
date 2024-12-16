<script lang="ts">
  export let isOpen: boolean = true;
  export let width: string = "250px";
</script>

<aside
  class="franken-sidebar"
  class:open={isOpen}
  style="--sidebar-width: {width}"
>
  <slot />
</aside>

<style lang="scss">
  @use "../styles/variables";

  .franken-sidebar {
    display: flex;
    flex-direction: column;
    top: 0;
    left: 0;
    height: 100vh;
    width: var(--sidebar-width);
    background-color: variables.$side-bar-bg-color;
    border-right: 1px solid variables.$side-bar-border-color;
    padding-top: 1rem;
    transition: transform 0.3s ease-in-out;
    z-index: 1000;

    &.open {
      transform: translateX(0);
    }
  }
</style>
