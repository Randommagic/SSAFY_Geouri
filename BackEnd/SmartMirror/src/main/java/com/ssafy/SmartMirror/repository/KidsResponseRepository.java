package com.ssafy.SmartMirror.repository;

import com.ssafy.SmartMirror.domain.AdultScript;
import com.ssafy.SmartMirror.domain.KidsResponse;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface KidsResponseRepository extends JpaRepository<KidsResponse, Long> {
    List<KidsResponse> findAllByReqKeyAndReaction(Long reqKey, int reaction);
    List<KidsResponse> findAllByReqKeyAndReactionAndResType(Long reqKey, int reaction, int type);
    List<KidsResponse> findAllByReactionAndResType(int reaction, int type);
}
