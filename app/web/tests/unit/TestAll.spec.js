import NavBarTop from "@/components/NavBarTop.vue";
import Logo from "@/components/Logo.vue";
import RobotsAll from "@/components/RobotsAll.vue";
import { shallowMount } from "@vue/test-utils";

fdescribe("Logo.vue", () => {
  let wrapper;
  beforeEach(() => {
    wrapper = shallowMount(Logo, {});
  });
  it("renders", () => {
    expect(wrapper.exists()).toBe(true);
  });
  it("check img", () => {
    const img = wrapper.findAll(".logo");
    expect(wrapper.findAll("img").exists()).toBe(true);
    expect(img.length).toBe(1);
  });
});

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
