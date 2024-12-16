<script lang="ts">
  interface NavItem {
    label: string;
    icon?: string;
    href?: string;
    isActive?: boolean;
    children?: NavItem[];
  }

  export let multiple: boolean = false;
  export let items: NavItem[] = [];
</script>

<ul class="uk-nav-primary" data-uk-nav="multiple: {multiple}">
  {#each items as item}
    <li class:uk-active={item.isActive} class:uk-parent={item.children?.length}>
      <a href={item.href || "#"}>
        {#if item.icon}
          <uk-icon width="20" height="20" icon={item.icon}></uk-icon>
        {/if}
        {item.label}
        {#if item.children?.length}
          <span data-uk-nav-parent-icon></span>
        {/if}
      </a>
      {#if item.children?.length}
        <ul class="uk-nav-sub">
          {#each item.children as child}
            <li class:uk-active={child.isActive}>
              <a href={child.href || "#"}>{child.label}</a>
              {#if child.children?.length}
                <ul>
                  {#each child.children as subChild}
                    <li class:uk-active={subChild.isActive}>
                      <a href={subChild.href || "#"}>{subChild.label}</a>
                    </li>
                  {/each}
                </ul>
              {/if}
            </li>
          {/each}
        </ul>
      {/if}
    </li>
  {/each}
</ul>

<style lang="scss">
  @use "../styles/variables";

  uk-icon {
    margin-right: 10px;
  }
</style>
