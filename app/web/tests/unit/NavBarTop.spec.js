import NavBarTop from "@/components/NavBarTop.vue";
import { shallowMount } from "@vue/test-utils";

fdescribe("NavBarTop.vue", () => {
  let wrapper;
  beforeEach(() => {
    wrapper = shallowMount(NavBarTop, {});
  });
  it("renders", () => {
    expect(wrapper.exists()).toBe(true);
  });
  it("check text", () => {
    expect(wrapper.text()).toBe("Au bon beurre");
  });
});
