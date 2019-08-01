import { shallowMount } from "@vue/test-utils";
import Pane from "@/components/Pane.vue";

describe("Pane.vue", () => {
  it("renders props.msg when passed", () => {
    const msg = "new message";
    const wrapper = shallowMount(Pane, {
      propsData: { msg }
    });
    expect(wrapper.text()).toMatch(msg);
  });
});
