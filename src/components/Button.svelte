<script lang="ts">
  import { cn } from "../lib/utils";
  import { ButtonVariant, ButtonSize, ButtonType } from "../lib/types/button";

  export let variant: ButtonVariant = ButtonVariant.Default;
  export let size: ButtonSize = ButtonSize.Default;
  export let type: ButtonType = ButtonType.Button;
  export let disabled = false;
  export let className: string = "";

  const sizes = {
    default: "btn-default",
    sm: "btn-sm",
    lg: "btn-lg",
    icon: "btn-icon",
  };

  $: buttonClass = cn("btn uk-button", variant, sizes[size], className);
</script>

<button {type} class={buttonClass} {disabled} {...$$restProps} on:click>
  <slot />
</button>

<style lang="scss">
  .btn {
    &-default {
      height: 40px;
      padding: 0 16px;
    }

    &-sm {
      height: 36px;
      padding: 0 12px;
    }

    &-lg {
      height: 44px;
      padding: 0 24px;
    }

    &-icon {
      height: 40px;
      width: 40px;
      padding: 0;
    }
  }
</style>
